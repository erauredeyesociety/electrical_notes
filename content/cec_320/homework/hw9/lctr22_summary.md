# Lecture 22: Increment Operations for Variables and Pointers in C and ASM

## C Operator Precedence (Key Levels)

| Precedence | Operators | Associativity |
|---|---|---|
| 1 (highest) | `()` `[]` `.` `->` postfix `++`/`--` | Left to right |
| 2 | prefix `++`/`--`, unary `+`/`-`, `!` `~`, `(type)`, `*` (deref), `&` (address), `sizeof` | **Right to left** |
| 3 | `*` `/` `%` | Left to right |
| 4 | `+` `-` | Left to right |
| 14 | `=` `+=` `-=` etc. | Right to left |

**Critical**: Postfix `++`/`--` is precedence 1 (highest). Prefix `++`/`--` is precedence 2, same level as dereference `*` and type cast, with **right-to-left** associativity.

---

## Prefix vs Postfix Increment on Variables

### Prefix `++A[0]`
1. Increment `A[0]` first
2. Then use the incremented value

### Postfix `A[1]++`
1. Use the current value of `A[1]` first
2. Then increment `A[1]`

### ASM implementation (R0=pA, R1=pB, passed as pointers)

`B[0] = ++A[0];` translates to:
```asm
ldr  r2, [r0]       @ temp = A[0]
add  r2, #1         @ temp++
str  r2, [r0]       @ A[0] = temp
str  r2, [r1]       @ B[0] = temp
```

`B[1] = A[1]++;` translates to:
```asm
ldr  r2, [r0, #4]   @ temp = A[1]
str  r2, [r1, #4]   @ B[1] = temp   (use BEFORE increment)
add  r2, #1         @ temp++
str  r2, [r0, #4]   @ A[1] = temp
```

---

## Compound Increment: `B[1] = A[i++]++;`

This is tricky. The correct interpretation:
1. Array index `[]` and postfix `++` on `i` are same precedence, left-to-right: `A[i++]` reads `A[i]`, then increments `i`
2. The second postfix `++` is bound to `A[i]` (the original index, not the incremented one): use value of `A[i]` for assignment, then increment `A[i]`

ASM (R0=pA, R1=pB, R2=pI; i in r3, temp in r4):
```asm
ldr  r3, [r2]              @ Load i
ldr  r4, [r0, r3, lsl #2]  @ temp = A[i]
str  r4, [r1, #4]          @ B[1] = temp
add  r4, #1                @ temp++
str  r4, [r0, r3, lsl #2]  @ A[i] = temp
add  r3, #1                @ i++
str  r3, [r2]              @ Save i
```

**WARNING**: Do not write code like `B[i] = A[i++]++;` -- it leads to unsequenced modification warnings and undefined behavior. Use separate statements instead:
```c
B[i] = A[i]++, i++;
```

---

## Issues with C Increment Operators

- `B[i] = A[i++]++;` -- **Warning**: unsequenced modification and access to `i`
- `B[i] = A[i]++++` -- **Error**: expression must be a modifiable lvalue
- Safe alternative: `B[i] = A[i]++, i++;` (use comma operator)
- Another safe form: `B[i] = A[i], A[i] += 2;`

---

## Simple Pointer Operations

### Pointer increment depends on data type
- `int16_t *p16`: `p16++` advances by 2 bytes (sizeof int16_t)
- `int32_t *p32`: `p32++` advances by 4 bytes (sizeof int32_t)

### Pointer difference depends on context
- With typed pointers: `p16 - A` gives offset in **elements** (e.g., 2 means 2 elements)
- With void pointers: `(void*)p16 - (void*)A` gives offset in **bytes** (e.g., 4 bytes)

### Example
```c
int16_t *p16 = &A[0];
int32_t *p32 = &B[0];
*p16++ = 0, *p16++ = 1;    // A[0]=0, A[1]=1, p16 now at &A[2]
*p32++ = 0, *p32++ = -1;   // B[0]=0, B[1]=-1, p32 now at &B[2]
// (p16 - A) == 2 (elements), ((void*)p16 - (void*)A) == 4 (bytes)
// (p32 - B) == 2 (elements), ((void*)p32 - (void*)B) == 8 (bytes)
```

---

## Pointer Type-Casting

When you cast a pointer to a different type, the increment size changes:
```c
*p16++ = *((int16_t *)p32 + i) << 2;
```
Here `p32` is cast to `int16_t *`, so `+i` advances by `i*2` bytes instead of `i*4`.

---

## Mixed Pointer and Other Operations

### `*p32++ = (int32_t)*p16++;`
- Read `*p16`, cast to 32-bit, store to `*p32`
- Both pointers advance (p16 by 2 bytes, p32 by 4 bytes)
- ASM: `ldrsh r2, [r0], #2` then `str r2, [r1], #4`

### `*p32++ = (int32_t)(*p16)++;`
- Read `*p16`, cast to 32-bit, store to `*p32`
- Then increment the VALUE at `*p16` (not the pointer), then advance p32
- ASM: `ldrsh r2, [r0]` / `str r2, [r1], #4` / `add r2, #1` / `strh r2, [r0]`

### `*++p32 = (int32_t)*++p16;`
- Pre-increment both pointers, then read and store
- ASM: `ldrsh r2, [r0, #2]!` then `str r2, [r1, #4]!`

### `*++p32 = (int32_t)++*++p16;`
- Pre-increment p16, read value, increment the value, cast, pre-increment p32, store
- ASM: `ldrsh r2, [r0, #2]!` / `add r2, #1` / `strh r2, [r0]` / `str r2, [r1, #4]!`
