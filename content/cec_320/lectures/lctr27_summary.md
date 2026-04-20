# Lctr 27 — Complex Flow Control in C and ASM

**Instructor:** Jianhua Liu
**Term:** Spring 2026
**Source:** `mp-hi-lctr27-complex-flow-control-in-c-n-asm-26-04.pdf`

This lecture extends the basic loop control of Lctr 26 (`for` / `while` / `do-while`) by introducing *complex* flow-altering keywords — `break`, `continue`, and the `switch` construct — together with their ARM assembly implementations. A new pair of ASM tools, the `ADR` and `TBB` instructions, is introduced to support efficient `switch` dispatch via a byte table.

---

## Core concepts

- The `break` and `continue` keywords for C and their implementation in ASM.
- The `switch` construct in C and two implementations in ASM (naive compare-and-branch ladder vs. table-based `TBB`).
- The `ADR` instruction for loading PC-relative labels (position-independent code).
- The `TBB` (table branch byte) and `TBH` (table branch halfword) instructions for compact switch dispatch.
- Motivation: removing code repetition that arises when preparing a compound `while` condition.

## Demo project

- Solutions of the in-class examples and exercises.
- Example 1 — `mp_swap_pairs_in_str_break`: the `while (1)` + `break` idiom that replaces a `while (ch1 && ch2)` loop with a pre-loop setup block.
- Example 2 — `mp_count_non_space_chars_in_str`: combined `break` + `continue` inside a `while (1)` to skip spaces and terminate on the null byte.
- Example 3 — `mp_letter_grade_to_pass_or_fail`: a `switch` mapping A/B/C → 'P', D/F → 'F', default → 'E', implemented two ways in ASM (naive and TBB).
- Exercise 1 — swap first and third letters of each trio in a string (solution in the demo project only).

## C and ASM programming

- The `ADR Rd, label` instruction for PC-relative label loading.
- The `TBB [Rn, Rm]` instruction: branches to `PC + 4 + 2 * table[Rm]` where `table` is a byte array at `Rn`.
- The `TBH` counterpart for larger switch tables (halfword entries instead of byte entries).

---

## 27.1 Introduction — why we need more than the basic loops

Lctr 26 ended with Exercise 1: write a C function that swaps every adjacent pair of chars in a string and returns the number of pairs swapped (e.g. `"noted"` → `"onetd"`, return `2`). The natural answer is a `while` loop with a compound condition:

```c
int mp_swap_pairs_in_str_c4s(char *str) {
    int pair_swapped = 0;
    char ch1 = *str++;
    char ch2 = *str;
    while (ch1 && ch2) {
        *str = ch1;
        *(str - 1) = ch2;
        ch1 = *++str;
        ch2 = *++str;
        pair_swapped++;
    }
    return pair_swapped;
}
```

The pre-loop setup (`char ch1 = *str++; char ch2 = *str;`) is nearly identical to the update at the bottom of the loop body (`ch1 = *++str; ch2 = *++str;`). That code duplication is an aesthetic and maintenance problem that the rest of the lecture removes.

The ASM translation of the compound `while (ch1 && ch2)` uses two `CBZ` instructions — if either byte is zero, we branch out of the loop:

```asm
mp_swap_pairs_in_str_c4s_s:
    ldr     r3, =0
    ldrb    r1, [r0], #1      @ ch1 = *str++
    ldrb    r2, [r0]          @ ch2 = *str
mp_swap_pairs_in_str_s_lp:
    cbz     r1, mp_swap_pairs_in_str_s_end
    cbz     r2, mp_swap_pairs_in_str_s_end
    strb    r1, [r0]
    strb    r2, [r0, #-1]
    ldrb    r1, [r0, #1]!
    ldrb    r2, [r0, #1]!
    add     r3, #1
    b       mp_swap_pairs_in_str_s_lp
mp_swap_pairs_in_str_s_end:
    mov     r0, r3
    bx      lr
```

Notice the asymmetry — the initial two `ldrb`s use a post-increment on only one of them, while inside the loop both use a pre-indexed write-back. That is the code repetition we want to eliminate.

---

## 27.2 The `break` keyword — jumping out of a loop

`break` changes the flow of any loop (`for`, `while`, or `do-while`) by jumping immediately out of it. Because C requires a conditional exit, `break` is always wrapped in an `if`.

The cleaner version of the swap-pairs function uses `while (1)` + `break`, collapsing the two identical-but-not-quite setup and update blocks into a single read at the top of every iteration:

```c
int mp_swap_pairs_in_str_break(char *str) {
    int pair_swapped = 0;
    while (1) {
        char ch1 = *str++;
        char ch2 = *str++;
        if (ch1 && ch2) {
            *(str - 1) = ch1;
            *(str - 2) = ch2;
            pair_swapped++;
        } else {
            break;
        }
    }
    return pair_swapped;
}
```

In ASM, `while (1)` is just a label plus an unconditional `b` at the end, and the `break` is a forward `b` (or, more economically, a `cbz` as soon as we detect the zero byte):

```asm
mp_swap_pairs_in_str_break_s:
    ldr     r3, =0
mp_swap_pairs_in_str_break_s_lp:
    ldrb    r1, [r0], #1      @ ch1 = *str++
    cbz     r1, mp_swap_pairs_in_str_break_s_end   @ break
    ldrb    r2, [r0], #1      @ ch2 = *str++
    cbz     r2, mp_swap_pairs_in_str_break_s_end   @ break
    strb    r1, [r0, #-1]
    strb    r2, [r0, #-2]
    add     r3, #1
    b       mp_swap_pairs_in_str_break_s_lp
mp_swap_pairs_in_str_break_s_end:
    mov     r0, r3
    bx      lr
```

Key takeaway: the `while (1)` construct and the `break` keyword require **no extra instructions** in ASM — they fall out naturally from the existing `b` / `cbz` toolkit.

`break` also appears inside `switch` to stop fall-through — see section 27.4.

---

## 27.3 The `continue` keyword — skipping to the next iteration

`continue` also skips code, but instead of leaving the loop it jumps to the *next iteration test*.

- In a `for` loop, `continue` jumps to the **update expression** (not directly to the test).
- In a `while` / `do-while` loop, `continue` jumps to the **condition test**. Because of that, any loop-variable update must be placed **before** the `continue`, or the loop will spin forever.

Example 2a combines `break` (to terminate on end-of-string) with `continue` (to skip spaces without counting them):

```c
int mp_count_non_space_chars_in_str(char *str) {
    int num_chars = 0;
    while (1) {
        char ch = *str++;
        if (ch == 0) {
            break;
        } else if (ch == ' ') {
            continue;
        }
        num_chars++;
    }
    return num_chars;
}
```

Note that the pointer increment `*str++` happens *before* the dispatch — so `continue` is safe here (the "update" already happened).

ASM translation (Example 2b). `continue` is just a backward `b` to the top of the loop; `break` is a forward `b` (or `cbz`) to the end:

```asm
mp_count_non_space_chars_in_str_s:
    ldr     r2, =0
mp_count_non_space_chars_in_str_s_lp:
    ldrb    r1, [r0], #1
    cbz     r1, mp_count_non_space_chars_in_str_s_end   @ break
    cmp     r1, #32                                     @ ' '
    beq     mp_count_non_space_chars_in_str_s_lp        @ continue
    add     r2, #1
    b       mp_count_non_space_chars_in_str_s_lp
mp_count_non_space_chars_in_str_s_end:
    mov     r0, r2
    bx      lr
```

Both `break` and `continue` are, at the ASM level, just well-placed `b` or conditional-branch instructions. There is no "break" opcode — the compiler arranges labels appropriately.

---

## 27.4 The `switch` construct

### 27.4.1 `switch` in C

Generic form:

```c
switch (expression) {
case constant1:
    // statements
    break;
case constant2:
    // statements
    break;
    ...
default:
    // default statements
}
```

Two rules:

- The `break` inside each case *prevents fall-through*. Removing it lets control drop into the next case — this is sometimes a deliberate feature (several case labels sharing a body, as in Example 3a below).
- `default:` is optional. Because it is the last block, it does not need a `break`.

Example 3a — letter grade to pass/fail, demonstrating stacked case labels with no body between them:

```c
char mp_letter_grade_to_pass_or_fail(char letter_grade) {
    char pass_fail_grade;
    switch (letter_grade) {
    case 'A':
    case 'B':
    case 'C':
        pass_fail_grade = 'P';  // Pass
        break;
    case 'D':
    case 'F':
        pass_fail_grade = 'F';  // Fail
        break;
    default:
        pass_fail_grade = 'E';  // Error
    }
    return pass_fail_grade;
}
```

### 27.4.2 The naive ASM approach — compare-and-branch ladder

Translate every case test as `cmp r0, #<ascii>` + `beq <case_label>`. An unconditional `b` to `default` follows the last test. Each case block ends with `b <end>` to mimic `break`, and stacked case labels simply fall through to the shared body:

```asm
mp_letter_grade_to_pass_or_fail_naive_s:
    cmp     r0, #65     @ 'A'
    beq     mp_letter_grade_to_pass_or_fail_naive_case_a
    cmp     r0, #66     @ 'B'
    beq     mp_letter_grade_to_pass_or_fail_naive_case_b
    cmp     r0, #67     @ 'C'
    beq     mp_letter_grade_to_pass_or_fail_naive_case_c
    cmp     r0, #68     @ 'D'
    beq     mp_letter_grade_to_pass_or_fail_naive_case_d
    cmp     r0, #70     @ 'F'
    beq     mp_letter_grade_to_pass_or_fail_naive_case_f
    b       mp_letter_grade_to_pass_or_fail_naive_default

mp_letter_grade_to_pass_or_fail_naive_case_a:
mp_letter_grade_to_pass_or_fail_naive_case_b:
mp_letter_grade_to_pass_or_fail_naive_case_c:
    ldr     r0, =80     @ 'P'
    b       mp_letter_grade_to_pass_or_fail_naive_end

mp_letter_grade_to_pass_or_fail_naive_case_d:
mp_letter_grade_to_pass_or_fail_naive_case_f:
    ldr     r0, =70     @ 'F'
    b       mp_letter_grade_to_pass_or_fail_naive_end

mp_letter_grade_to_pass_or_fail_naive_default:
    ldr     r0, =69     @ 'E'

mp_letter_grade_to_pass_or_fail_naive_end:
    bx      lr
```

Clean and readable, but the repeated `cmp` / `beq` is slow when there are many cases — it is `O(n)` in the number of cases.

### 27.4.3 The TBB-based ASM approach

#### The `ADR` instruction

`ADR{cond} Rd, label` loads the **PC-relative address** of `label` into `Rd`. It is the standard way to obtain a pointer to a local ASM table while keeping the code position-independent (no absolute address baked into a literal pool).

#### The `TBB` instruction

```asm
TBB  [Rn, Rm]
```

`Rn` points to a byte table. `Rm` is the index. The instruction branches to:

```
PC + 4 + 2 * mp_tbb_table[Rm]
```

The doubling is because Thumb-2 instructions are halfword-aligned — every valid branch target has an even address, so storing *halved* offsets in the table lets one byte cover a 512-byte jump range from the TBB. `Rm` must be between `0` and `n - 1` for an `n`-entry table; callers must range-check beforehand.

`TBH` (table branch halfword) is the same idea with 16-bit entries, for switch tables whose entries span more than 512 bytes of code.

#### Example 3c — letter-grade switch with TBB

Subtract `'A'` from the letter first, so the switch index is in `0..5`; range-check (`<0` or `>=6` → default); use `ADR` to load the table address; `TBB` dispatches in one instruction:

```asm
mp_letter_grade_to_pass_or_fail_tbb_s:
    sub     r0, #65             @ r0 = letter_grade - 'A'  => 0..5
    cmp     r0, #0
    blt     mp_tbb_default
    cmp     r0, #6
    bge     mp_tbb_default
    adr     r1, mp_tbb_table
    tbb     [r1, r0]

mp_tbb_case_a:
mp_tbb_case_b:
mp_tbb_case_c:
    ldr     r0, =80     @ 'P' for pass
    b       mp_letter_grade_to_pass_or_fail_tbb_end

mp_tbb_case_d:
mp_tbb_case_f:
    ldr     r0, =70     @ 'F' for fail
    b       mp_letter_grade_to_pass_or_fail_tbb_end

mp_tbb_default:
    ldr     r0, =69     @ 'E' for error

mp_letter_grade_to_pass_or_fail_tbb_end:
    bx      lr

mp_tbb_table:
    .byte   0                                       @ r0 = 0, 'A'
    .byte   (mp_tbb_case_b - mp_tbb_case_a) / 2     @ r0 = 1, 'B'
    .byte   (mp_tbb_case_c - mp_tbb_case_a) / 2     @ r0 = 2, 'C'
    .byte   (mp_tbb_case_d - mp_tbb_case_a) / 2     @ r0 = 3, 'D'
    .byte   (mp_tbb_default - mp_tbb_case_a) / 2    @ r0 = 4, 'E' (hole: no letter E in A..F)
    .byte   (mp_tbb_case_f - mp_tbb_case_a) / 2     @ r0 = 5, 'F'
```

Notes on the table entries:

- Entry 0 is `0` — because the TBB base is computed as `PC + 4`, landing the zero offset on the instruction immediately after `TBB`, which is `mp_tbb_case_a`.
- Entry 4 routes to `mp_tbb_default`. This fills the *hole* between `'D'` and `'F'` (there is no `'E'` in the expected letters) so that invalid-but-in-range indices land on the default handler.
- All offsets are divided by 2 because `TBB` multiplies by 2 when it computes the target (halfword alignment).

The TBB form is compact (1 byte per case + one `TBB` instruction) and constant-time regardless of case count.

### 27.4.4 TBH — table branch halfword

`TBH` is the halfword counterpart of `TBB`. Same mechanics, but table entries are 16 bits, allowing switch constructs with a larger total jump span than `TBB` can express.

---

## 27.5 Class exercise

**Exercise 1a.** Write a C function that swaps the first and third letters of every trio in a string without calling library functions; return the number of trios swapped. Examples:

- `"not"` → `"ton"`, return `1`.
- `"note"` → `"tone"`, return `1`.
- `"noted"` → `"toned"`, return `1`.
- `"denote"` → `"nedeto"`, return `2`.

**Exercise 1b.** Translate the above into ASM.

The pattern mirrors Example 1: a `while (1)` loop with an early `break` when the trio is incomplete (null terminator appears at position 1 or 3). See the demo project for solutions.

---

## Cross-references

- Lctr 19 — conditional branches (`b`, `beq`, `bne`, `blt`, `bge`) that `break` / `continue` lower into.
- Lctr 24 — `CBZ` / `CBNZ` used throughout this lecture for fast zero tests on `char` reads.
- Lctr 25 — if-based flow control; `switch` is the dispatching alternative.
- Lctr 26 — the basic `for` / `while` / `do-while` loops that `break` and `continue` modify.
- HW12 — applies these patterns to string-manipulation problems similar to the lecture exercises.
