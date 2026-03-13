This walkthrough covers the problems in **Homework 8 (FMFO NZCV and More)**, which focuses on processor status flags, condition code suffixes (CCS), and implementing C flow control in Assembly.

---

### **Problem 1: 5-bit Signed/Unsigned Operations**
This problem requires determining the results of arithmetic operations in a 5-bit system ($N=5$).
**Constants for 5-bit system:** $C_N = 2^5 = 32$; Unsigned Range =; Signed Range = [-16, 15].

#### **(a) $(-15) + (-5)$**
1.  **Unsigned Interpretation ($u_{temp}$):**
    *   $-15$ in 5-bit unsigned is $-15 + 32 = 17$.
    *   $-5$ in 5-bit unsigned is $-5 + 32 = 27$.
    *   $17 + 27 = 44$. Since $44 > 31$, there is a **Carry** ($C=1$).
    *   Corrected result: $44 - 32 = \mathbf{12}$.
2.  **Signed Interpretation ($s_{temp}$):**
    *   $(-15) + (-5) = -20$.
    *   Since $-20 < -16$ (below $S_{min}$), there is an **Overflow** ($\mathbf{V=1}$).
    *   Corrected result: $-20 + 32 = \mathbf{12}$.
3.  **Status Flags:**
    *   **N (Negative):** Result is 12 ($0b01100$). MSB is 0, so **N = 0**.
    *   **Z (Zero):** Result is 12 (non-zero), so **Z = 0**.
    *   **C = 1** (Carry occurred).
    *   **V = 1** (Overflow occurred).
4.  **Binary Result:** **$0b01100$**.

#### **(b) $11 - 18$**
1.  **Unsigned Interpretation ($s_{temp}$):**
    *   $11 - 18 = -7$. Since $-7 < 0$, there is a **Borrow**, meaning **C = 0** ($C = 1 - B$).
    *   Corrected result: $-7 + 32 = \mathbf{25}$.
2.  **Signed Interpretation ($s_{temp}$):**
    *   $11 - (18 - 32) = 11 - (-14) = 25$.
    *   Since $25 > 15$ (above $S_{max}$), there is an **Overflow** ($\mathbf{V=1}$).
    *   Corrected result: $25 - 32 = \mathbf{-7}$.
3.  **Status Flags:**
    *   **N:** Result is -7 ($0b11001$). MSB is 1, so **N = 1**.
    *   **Z:** Result is non-zero, so **Z = 0**.
    *   **C = 0** (Borrow occurred).
    *   **V = 1** (Overflow occurred).
4.  **Binary Result:** **$0b11001$**.

---

### **Problem 2: 6-bit Comparison and CCS Verification**
**Constants for 6-bit system:** $C_N = 64$.
**Operation:** `CMP r0, r1` (performs `r0 - r1` and updates flags without storing the result).

#### **Case (a): $r0 = 22, r1 = 20$**
1.  **Flags:** $22 - 20 = 2$.
    *   **N = 0** (positive), **Z = 0** (non-zero), **C = 1** (No borrow, $22 \ge 20$), **V = 0** (No overflow, $2 \in [-32, 31]$).
2.  **CCS Verification:**
    *   **GT** ($V == N$ and $Z == 0$): $0==0$ and $0==0 \rightarrow$ **True**.
    *   **HI** ($C == 1$ and $Z == 0$): $1==1$ and $0==0 \rightarrow$ **True**.

#### **Case (b): $r0 = -20, r1 = -22$**
1.  **Flags:** $-20 - (-22) = 2$.
    *   Unsigned check: $-20 \rightarrow 44$; $-22 \rightarrow 42$. $44 - 42 = 2$.
    *   **N = 0**, **Z = 0**, **C = 1** (No borrow), **V = 0** (No overflow).
2.  **CCS Verification:** Results are identical to Case (a) because both interpret the difference as 2.

#### **Logic Equations for EQ and NE:**
*   **EQ** $\iff$ **(Z == 1)**
*   **NE** $\iff$ **(Z == 0)**

---

### **Problem 3: Assembly Implementation of `mp_max_ab_i_s`**
**Requirement:** Implement `if (a >= b) return a; else return b;` for signed integers.

**Register Mapping:** `a` $\rightarrow$ R0, `b` $\rightarrow$ R1.
**Logic:** Compare R0 and R1. If R0 is less than R1 (Negative Logic for `GE`), branch to the `else` block.

```assembly
@ int mp_max_ab_i_s(int a, int b)
@ Input: a -> r0, b -> r1
@ Output: r0
mp_max_ab_i_s:
    cmp r0, r1                  @ Compare a and b
    blt mp_max_ab_i_s_else      @ If a < b, branch to else
mp_max_ab_i_s_then:
    @ result is already in r0 (a)
    b mp_max_ab_i_s_end_if      @ Branch to return
mp_max_ab_i_s_else:
    mov r0, r1                  @ move b to r0 for return
mp_max_ab_i_s_end_if:
    bx lr                       @ Return
```

---

### **Problem 4: Assembly Implementation of a `while` Loop**
**Requirement:** Sum range $[s, e]$ using a standard `while` loop.

**Register Mapping:** `s` $\rightarrow$ R0, `e` $\rightarrow$ R1, `sum` $\rightarrow$ R2, `i` $\rightarrow$ R3.

```assembly
@ int mp_range_sum_standard_while_s(int s, int e)
@ Input: s -> r0, e -> r1
@ Output: r0 (sum)
mp_range_sum_standard_while_s:
    mov r2, #0                  @ sum = 0
    mov r3, r0                  @ i = s
mp_range_sum_loop:
    cmp r3, r1                  @ Compare i and e
    bgt mp_range_sum_end        @ If i > e, exit loop
    add r2, r2, r3              @ sum += i
    add r3, r3, #1              @ i++
    b mp_range_sum_loop         @ Repeat loop
mp_range_sum_end:
    mov r0, r2                  @ Put sum in return register
    bx lr                       @ Return
```