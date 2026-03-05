// Initializing the PRN register---dereferenced prn_reg
uint32_t mp_prn_ini_c(uint32_t *prn_reg, int *poly, int poly_n) {
    // Find the max value in poly[] to determine bit width
    int max_val = poly[0];
    for (int i = 1; i < poly_n; i++) {
        if (poly[i] > max_val) max_val = poly[i];
    }
    // reg_mask = (1 << max_val) - 1, all 1s for max_val bits
    reg_mask = (1U << max_val) - 1;
    // Initialize the shift register to all 1s
    *prn_reg = reg_mask;
    return reg_mask;
}

// Building the tap mask from poly and poly_n
uint32_t mp_prn_tap_mask_c(int *poly, int poly_n) {
    tap_mask = 0;
    for (int i = 0; i < poly_n; i++) {
        tap_mask |= (1U << (poly[i] - 1));
    }
    return tap_mask;
}

// Generating the output bit and updating prn_reg
bool mp_prn_gen_c(uint32_t *prn_reg) {
    uint32_t val = *prn_reg;
    // Tap bits using tap_mask
    uint32_t tapped = val & tap_mask;
    // Sum the 1s; feedback = XOR of tapped bits = sum_of_1s & 1
    uint32_t feedback = mp_sum_of_1s(tapped) & 1U;
    // Output bit = MSB of the n-bit register
    // reg_mask = (1<<n)-1, so (reg_mask+1)>>1 = (1<<(n-1)) is the MSB bit
    bool output = (val & ((reg_mask + 1) >> 1)) ? true : false;
    // Shift register left by 1 (LSB to MSB)
    val = val << 1;
    // OR feedback into LSB
    val = val | feedback;
    // Mask to keep within bit width
    val = val & reg_mask;
    // Write back
    *prn_reg = val;
    return output;
}
