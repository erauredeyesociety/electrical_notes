## Problem 1

### Setup: Register Mapping (AAPCS)

For `x_cmp_y_load(int32_t x, int32_t y, int16_t *ptrA, int32_t *ptrB)`:

| Register | Argument | Type |
|----------|----------|------|
| `r0` | `x` | `int32_t` |
| `r1` | `y` | `int32_t` |
| `r2` | `ptrA` | `int16_t *` |
| `r3` | `ptrB` | `int32_t *` |

Return value goes in `r0`. Because `x` and `y` are signed, we use signed condition codes (`GT`, `LE`). Because `*ptrB / 2` is a signed divide (`ptrB` is `int32_t *`), we use `ASR` — not `LSR`.

**Per-branch translation:**

- **Then branch** — `return (int32_t)*(++ptrA) * 2;`
  - Prefix `++ptrA`: advance `ptrA` by `sizeof(int16_t) = 2` bytes *before* loading so pre-indexed `ldrsh r0, [r2, #2]!`.
  - `(int32_t)*ptrA`: `LDRSH` sign-extends the halfword to 32 bits automatically.
  - `* 2`: `lsl r0, r0, #1`.
- **Else branch** — `return *(ptrB++) / 2;`
  - Postfix `ptrB++`: load from the *old* `ptrB`, then advance by `sizeof(int32_t) = 4` so post-indexed `ldr r0, [r3], #4`.
  - `/ 2` (signed): `asr r0, r0, #1`.

---

### Part 1 Positive Logic

Positive logic branches to `then` when the C test (`x > y`, signed) is true, so the `else` block is laid out first.

```asm
x_cmp_y_load_pl:            @ PL stands for positive logic
    cmp     r0, r1
    bgt     x_cmp_y_load_pl_then    @ if x > y, take then branch
x_cmp_y_load_pl_else:
    @ return *(ptrB++) / 2;
    ldr     r0, [r3], #4            @ r0 = *ptrB; ptrB++  (post-indexed)
    asr     r0, r0, #1              @ r0 = r0 / 2         (signed)
    b       x_cmp_y_load_pl_end
x_cmp_y_load_pl_then:
    @ return (int32_t)*(++ptrA) * 2;
    ldrsh   r0, [r2, #2]!           @ ptrA++; r0 = (int32_t)*ptrA  (pre-indexed, sign-ext)
    lsl     r0, r0, #1              @ r0 = r0 * 2
x_cmp_y_load_pl_end:
    bx      lr
```

**Why `BGT`:** the C test `x > y` on signed integers maps to the signed CCS `GT` (Lctr 19 / Lctr 25, Sec 25.3).

---

### Part 2 Negative Logic

Negative logic branches to `else` when the C test is *false* (i.e., `x <= y`), so the `then` block is laid out first.

```asm
x_cmp_y_load_nl:            @ NL stands for negative logic
    cmp     r0, r1
    ble     x_cmp_y_load_nl_else    @ if x <= y (opposite of C), take else branch
x_cmp_y_load_nl_then:
    @ return (int32_t)*(++ptrA) * 2;
    ldrsh   r0, [r2, #2]!           @ ptrA++; r0 = (int32_t)*ptrA
    lsl     r0, r0, #1              @ r0 = r0 * 2
    b       x_cmp_y_load_nl_end
x_cmp_y_load_nl_else:
    @ return *(ptrB++) / 2;
    ldr     r0, [r3], #4            @ r0 = *ptrB; ptrB++
    asr     r0, r0, #1              @ r0 = r0 / 2 (signed)
x_cmp_y_load_nl_end:
    bx      lr
```

**Why `BLE`:** negative logic uses the inverse of `GT`, which is `LE` (Lctr 25, Sec 25.3).

---

### Part 3 CEX Approach

With CEX under negative logic, the `else`-branch instructions are the `T` (matching) instructions (with CCS `LE`), and the `then`-branch instructions are the `E` (inverse) instructions (with CCS `GT`). Each branch needs two instructions (load + shift), so we use an `ITTEE` block (Lctr 24, Sec 24.3.2).

```asm
x_cmp_y_load_cex:           @ CEX: conditional execution
    cmp     r0, r1
    ittee   le              @ T=le, T=le, E=gt, E=gt
    ldrle   r0, [r3], #4    @ else: r0 = *ptrB; ptrB++
    asrle   r0, r0, #1      @ else: r0 = r0 / 2
    ldrshgt r0, [r2, #2]!   @ then: ptrA++; r0 = (int32_t)*ptrA
    lslgt   r0, r0, #1      @ then: r0 = r0 * 2
    bx      lr
```

**Why `ITTEE le`:**
- The CCS in `IT..` is `le` — the inverse of the C test `x > y` (this is the "negative logic" the problem asked for).
- `T` slots (1 and 2) run when `le` is true so they implement the C `else` branch.
- `E` slots (3 and 4) run when `gt` is true (inverse of `le`) so they implement the C `then` branch.
- Pre-indexed (`ldrshgt`) and post-indexed (`ldrle`) conditional LDRs are both supported (Lctr 24, Examples 3 and 4).

---

## Problem 2

### Setup

The piecewise math function is:

```
         | -10,  x < -5
f(x) =   |  10,  x >= 5
         |  2x,  otherwise  (i.e., -5 <= x < 5)
```

`r0` holds the input `x` and also the return value. `x` is a signed `int`, so we use signed CCSs.

---

### Part 1 C Implementation

```c
int mathf_c(int x) {
    int y;
    if (x < -5) {
        y = -10;
    } else if (x >= 5) {
        y = 10;
    } else {
        y = 2 * x;
    }
    return y;
}
```

This follows the straightforward `if-else-if-else` construct from Lctr 25, Sec 25.4.

---

### Part 2 CMP Approach

Each range of the piecewise function gets its own label. The chain of `CMP`/conditional-branch mirrors the C control flow.

```asm
mathf_cmp:
    cmp     r0, #-5                 @ check x < -5 (assembler: cmn r0, #5)
    bge     mathf_cmp_elseif        @ if x >= -5, skip to next test
mathf_cmp_then:
    ldr     r0, =-10                @ x < -5 : return -10
    b       mathf_cmp_end
mathf_cmp_elseif:
    cmp     r0, #5                  @ check x >= 5
    blt     mathf_cmp_else          @ if x < 5, go to else (2x)
    ldr     r0, =10                 @ x >= 5 : return 10
    b       mathf_cmp_end
mathf_cmp_else:
    lsl     r0, r0, #1              @ otherwise : return 2*x
mathf_cmp_end:
    bx      lr
```

**Notes:**
- `cmp r0, #-5` is assembled as `cmn r0, #5`; signed CCSs work unchanged (Lctr 25 / Lctr 18).
- `LDR Rd, =imm` is the literal-pool pseudo-instruction — the assembler picks `MOV` or a literal-pool load as needed.

---

### Part 3 CEX Approach

This uses the chained-IT pattern from Lctr 25 Example 4: an `ITT lt` whose second slot is a conditional `B` handles the `x < -5` case, and an `ITE ge` handles the remaining `x >= 5` vs. default `2x` split. The intermediate result lives in `r1` so the original `x` in `r0` stays available for the second test.

```asm
mathf_cex:
    cmp     r0, #-5                 @ first test: x < -5 ?
    itt     lt
    ldrlt   r1, =-10                @ T1: if x < -5, stash -10 in r1
    blt     mathf_cex_end           @ T2: and short-circuit to end
    @ fall-through: x >= -5
    cmp     r0, #5                  @ second test: x >= 5 ?
    ite     ge
    ldrge   r1, =10                 @ T : if x >= 5, stash 10 in r1
    lsllt   r1, r0, #1              @ E : otherwise, r1 = 2*x
mathf_cex_end:
    mov     r0, r1                  @ move result into return register
    bx      lr
```

**Notes:**

- `ITT lt`: both slots are conditional on `lt`. The second slot is a conditional `B`, which Lctr 24 explicitly allows at the end of an IT block.
- After the fall-through, the second `CMP` sets fresh flags, so the `ITE ge` is independent.
- `lsllt r1, r0, #1` is the else-of-the-inner-test — it uses the original `x` in `r0` (not `r1`), which is why we kept `x` in `r0`.

---

## Problem 3

### Setup: Register Mapping

For `load_based_on_x_c(int x, uint16_t *ptrA, uint32_t *ptrB)`:

| Register | Argument | Type |
|----------|----------|------|
| `r0` | `x` | `int` (signed) |
| `r1` | `ptrA` | `uint16_t *` |
| `r2` | `ptrB` | `uint32_t *` |

Key per-branch translations:

- **Then branch** — `return (int32_t)*++ptrA * 4;`
  - `*++ptrA`: pre-indexed `LDRH` with offset `#2` (since `sizeof(uint16_t) = 2`) — zero-extends.
  - Cast to `int32_t` of a non-negative value is trivial (zero extension already done by `LDRH`).
  - `* 4`: `lsl #2`.
- **Else branch** — `return *++ptrB / 4;`
  - `*++ptrB`: pre-indexed `LDR` with offset `#4` (since `sizeof(uint32_t) = 4`).
  - `/ 4` on a `uint32_t`: unsigned divide → `lsr #2` (not `asr`).

The test `x <= 20 || x >= 25` is a compound **OR** on signed `x` — use signed CCSs (`LE`, `GE`, and their inverses `GT`, `LT`).

---

### Part 1 CMP Approach

We use the short-circuit double-`CMP` pattern from Lctr 25 Example 6. If the first condition (`x <= 20`) is true, we jump straight into the `then` block without evaluating the second; otherwise, we evaluate `x >= 25`.

```asm
load_based_on_x_cmp:
    cmp     r0, #20
    ble     load_based_on_x_cmp_then    @ first cond true → then
    cmp     r0, #25
    bge     load_based_on_x_cmp_then    @ second cond true → then
    b       load_based_on_x_cmp_else    @ neither → else
load_based_on_x_cmp_then:
    @ return (int32_t)*++ptrA * 4;
    ldrh    r0, [r1, #2]!               @ ptrA++; r0 = *ptrA (zero-ext)
    lsl     r0, r0, #2                  @ r0 * 4
    b       load_based_on_x_cmp_end
load_based_on_x_cmp_else:
    @ return *++ptrB / 4;
    ldr     r0, [r2, #4]!               @ ptrB++; r0 = *ptrB
    lsr     r0, r0, #2                  @ r0 / 4 (unsigned)
load_based_on_x_cmp_end:
    bx      lr
```

---

### Part 2 CEX Approach (as much as possible)

The first sub-test (`x <= 20`) must be handled with a regular branch because an IT block cannot contain a conditional branch anywhere except the final slot — and we'd be entering the then-block body after that branch. After the fall-through, the second sub-test (`x >= 25`) drives a full `ITTEE ge` block that packs all four remaining instructions (two for `then`, two for `else`).

```asm

load_based_on_x_cex:
    cmp     r0, #20
    bgt     load_based_on_x_cex_check25 @ if x > 20, go to second test
    @ x <= 20 : compound is true → take then branch
    ldrh    r0, [r1, #2]!               @ ptrA++; r0 = *ptrA
    lsl     r0, r0, #2                  @ r0 * 4
    bx      lr
load_based_on_x_cex_check25:
    cmp     r0, #25
    ittee   ge                          @ T,T match ge; E,E match lt
    ldrhge  r0, [r1, #2]!               @ then: ptrA++; r0 = *ptrA
    lslge   r0, r0, #2                  @ then: r0 * 4
    ldrlt   r0, [r2, #4]!               @ else: ptrB++; r0 = *ptrB
    lsrlt   r0, r0, #2                  @ else: r0 / 4
    bx      lr
```

**Notes:**
- The second sub-test is `x >= 25` so CCS `ge` is the "condition is true" case (take the C `then` branch).
- `T` slots run when `ge` is true so the two then-branch instructions.
- `E` slots run when `lt` is true (inverse of `ge`) so the two else-branch instructions.
- Pre-indexed conditional `LDRH`/`LDR` are supported (Lctr 24, Example 4 shows `ldrhhi r0, [r2, #4]!`).

