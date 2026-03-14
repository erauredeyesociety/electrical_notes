Based on the provided source materials (HW 5/6 and Lectures 12/13), here are the solutions to all problems in Homework 5/6 with the required steps and references.

### **Problem 1: Encode 2.75 using UQ3.5 and write the result in hexadecimal.**

1.  **Identify the Format:** The format is **UQ3.5**, meaning an **unsigned** fixed-point number with **m = 3** integer bits and **n = 5** fractional bits. The total number of bits is **N = m + n = 8 bits**.
2.  **Scale the Number:** Multiply the real number ($f = 2.75$) by the scaling factor ($2^n = 2^5 = 32$):
    *   $2.75 \times 32 = \mathbf{88}$.
3.  **Round to Integer:** The result is already an integer, so $I = 88$.
4.  **Convert to Hexadecimal:**
    *   $88$ in binary (8-bit) is `0b0101_1000`.
    *   Converting to hexadecimal: `0b0101` = **5**, `0b1000` = **8**.
5.  **Final Result:** **0x58**.

---

### **Problem 2: Decode the following Q3.4 code back to real numbers: (a) $C_1 = 0x77$ and (b) $C_2 = 0xAA$**

**Part (a): $C_1 = 0x77$**
1.  **Identify the Format:** **Q3.4** is a **signed** fixed-point number with **1 sign bit**, **m = 3** integer bits, and **n = 4** fractional bits. Total bits **N = 8**.
2.  **Convert to Binary:** $0x77 = \mathbf{0b0111\_0111}$.
3.  **Find Signed Integer ($I_A$):** The MSB is **0**, so the number is positive. $I_A = U_A = 0x77 = \mathbf{119}$.
4.  **Scale back to Real ($f_A$):** Multiply by $2^{-n} = 2^{-4} = 1/16$:
    *   $119 \times (1/16) = \mathbf{7.4375}$.
5.  **Final Result:** **7.4375**.

**Part (b): $C_2 = 0xAA$**
1.  **Convert to Binary:** $0xAA = \mathbf{0b1010\_1010}$.
2.  **Find Signed Integer ($I_A$):** The MSB is **1**, so the number is negative. Use the **decimal TC approach**: $I_A = U_A - 2^N = 170 - 256 = \mathbf{-86}$.
3.  **Scale back to Real ($f_A$):** Multiply by $2^{-4} = 1/16$:
    *   $-86 \times (1/16) = \mathbf{-5.375}$.
4.  **Final Result:** **-5.375**.

---

### **Problem 3: Decode Q2.5 code 0b1001_1001 to real number.**

1.  **Identify the Format:** **Q2.5** is a signed fixed-point number ($m = 2, n = 5, N = 8$).
2.  **Determine MSB:** The binary data is **0b1001_1001**. The MSB is **1**, indicating a negative number.
3.  **Find Signed Integer ($I_A$):**
    *   Unsigned value ($U_A$): $128 + 16 + 8 + 1 = 153$.
    *   $I_A = U_A - 2^N = 153 - 256 = \mathbf{-103}$.
4.  **Scale to Real ($f_A$):** Multiply by $2^{-5} = 1/32$:
    *   $-103 \times (1/32) = \mathbf{-3.21875}$.
5.  **Final Result:** **-3.21875**.

---

### **Problem 4: Encode the following real numbers into Q3.4 format and write the results in hexadecimal: (a) $f_1 = 0.5$, (b) $f_2 = 6.73$, (c) $f_3 = -2.25$, and (d) $f_4 = -4.5$.**

1.  **Format Rules:** **Q3.4** is signed, $N = 8, n = 4$. Scaling factor = **16**.

**Step-by-Step Encoding:**
*   **(a) $f_1 = 0.5$:**
    1.  Scale: $0.5 \times 16 = 8$.
    2.  Binary (8-bit): `0b0000_1000`.
    3.  Hex: **0x08**.
*   **(b) $f_2 = 6.73$:**
    1.  Scale: $6.73 \times 16 = 107.68$.
    2.  Round: **108**.
    3.  Hex ($108 = 0x6C$): **0x6C**.
*   **(c) $f_3 = -2.25$:**
    1.  Scale: $-2.25 \times 16 = -36$.
    2.  Find TC ($N=8$): $-36 + 256 = 220$.
    3.  Hex ($220 = 0xDC$): **0xDC**.
*   **(d) $f_4 = -4.5$:**
    1.  Scale: $-4.5 \times 16 = -72$.
    2.  Find TC: $-72 + 256 = 184$.
    3.  Hex ($184 = 0xB8$): **0xB8**.

---

### **Problem 5: Assume we use Q15 to express real numbers $f_1 = 0.5, f_2 = 0.25, f_3 = 0.125, f_4 = 0.0625$. Perform: $f_A = f_1 \times f_2 + f_3 \times f_4$ in Q15.**

**Step 1: Encode $f_1$ to $f_4$ in Q15 ($n=15$)**.
1.  $I_1 = 0.5 \times 2^{15} = 16384$ (**0x4000**)
2.  $I_2 = 0.25 \times 2^{15} = 8192$ (**0x2000**)
3.  $I_3 = 0.125 \times 2^{15} = 4096$ (**0x1000**)
4.  $I_4 = 0.0625 \times 2^{15} = 2048$ (**0x0800**)

**Step 2: Perform Multiplications ($I_C = (I_A \times I_B) >> n$)**.
1.  **Product 1 ($I_{p1}$):** $(16384 \times 8192) >> 15 = 134,217,728 >> 15 = \mathbf{4096}$ (**0x1000**).
2.  **Product 2 ($I_{p2}$):** $(4096 \times 2048) >> 15 = 8,388,608 >> 15 = \mathbf{256}$ (**0x0100**).

**Step 3: Add the products ($I_A = I_{p1} + I_{p2}$)**.
1.  $I_A = 4096 + 256 = \mathbf{4352}$ (**0x1100**).

**Step 4: Decode $I_A$ to obtain $f_A$ ($f = I \times 2^{-n}$)**.
1.  $f_A = 4352 \times 2^{-15} = 4352 / 32768 = \mathbf{0.1328125}$.
2.  **Final Result:** **0.1328125**.