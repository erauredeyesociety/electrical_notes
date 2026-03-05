float mp_uq_and_q_mn_decoding(uint32_t D, int s, int m, int n) {
    int total_bits = m + n + s;  // s=1 adds sign bit for Qm.n
    uint32_t mask = (1U << total_bits) - 1;
    D = D & mask;  // mask to relevant bits

    float f;
    if (s && (D >> (total_bits - 1))) {
        // Signed Qm.n and sign bit is set: negative number
        // Sign-extend and convert via two's complement
        int32_t signed_D = (int32_t)(D | (~mask));
        f = (float)signed_D / (float)(1 << n);
    } else {
        // Unsigned UQm.n or positive Qm.n
        f = (float)D / (float)(1 << n);
    }
    return f;
}

uint32_t mp_uq_and_q_mn_encoding(float f, int s, int m, int n) {
    float fn = f * (1 << n);
    int32_t intD = lrint(fn);
    uint32_t D = (uint32_t)intD;
    return D;
}

float mp_q_mn_multiplication(float f1, float f2, int m, int n) {
    // Encode both operands to Qm.n (signed)
    int I1 = (int) mp_uq_and_q_mn_encoding(f1, 1, m, n);
    int I2 = (int) mp_uq_and_q_mn_encoding(f2, 1, m, n);
    // Multiply fixed-point values and shift right by n
    int I3 = I1 * I2;
    I3 >>= n;
    // Decode result back to float
    float prod = mp_uq_and_q_mn_decoding(I3, 1, m, n);
    return prod;
}
