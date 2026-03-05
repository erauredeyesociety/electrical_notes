void mp_app(void) {
    printf("\n\nRunning ee4u main App-----------------\n");

    float f1 = 0.5, f2 = 0.25, f3 = -0.625;

    // Encode to Q15 (m=0, n=15, signed)
    uint16_t I1 = mp_uq_and_q_mn_encoding(f1, 1, 0, 15);
    uint16_t I2 = mp_uq_and_q_mn_encoding(f2, 1, 0, 15);
    uint16_t I3 = mp_uq_and_q_mn_encoding(f3, 1, 0, 15);

    // Compute fA = f1 * f2 * f3 using Q15 multiplication
    float temp = mp_q_mn_multiplication(f1, f2, 0, 15);
    float f_A = mp_q_mn_multiplication(temp, f3, 0, 15);

    // Compute using direct float multiplication
    float f_A_float = f1 * f2 * f3;

    // Print results
    printf("I1 = 0x%04X, I2 = 0x%04X, I3 = 0x%04X \n", I1, I2, I3);
    printf("f_A_float = %8.7f, f_A = %8.7f \n", f_A_float, f_A);

    while (1);
}
