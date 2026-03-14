// PT1. Update type of candle: random or deterministic
void update_candle_type(void) {
    if (!has_new_command) {
        return;
    }
    // We will be here only if we receive a new command.
    // With this trick, we can reduce one level of code indentation below.
    command = uart2_rxBuffer[0];
    if (is_rdm_candle) {
        if (command == 'd') {
            is_rdm_candle = false;
            has_new_command = false;
        }
    } else {
        if (command == 'r') {
            is_rdm_candle = true;
            has_new_command = false;
        }
    }
    printf("Candle type is %s\n", is_rdm_candle? "Random":"Deterministic");
}


// PT2. Update the deterministic candle state
void update_det_candle_state(void) {
    if (!has_new_command || is_rdm_candle) {
        return;
    }
    // Update the new deterministic candle state
    command = uart2_rxBuffer[0];
    if (command >= '1' && command <= '4') {
        candle_state = (candle_state_t)(command - '1');
        has_new_command = false;
    }
    printf("Candle state is %d\n", candle_state+1);
}


// PT3. Create the cumulative transition matrix from the
// state transition probability matrix.
void create_cumu_trans_matrix(void) {
    for (int i = 0; i < 4; i++) {
        float F = 0.0;   // Cumulative prob distribution
        for (int j = 0; j < 4; j++) {
            F += trans_prob[i][j];
            cumu_trans_matrix[i][j] = lrint(F * STATE_TRANS_RANGE);
            printf("\t%d, ", cumu_trans_matrix[i][j]);
        }
        printf("\n");
    }
}


// PT4. LED candle state machine
void update_random_candle_state(void) {
    if (!is_rdm_candle) {
        return;
    }
    int random_choice = rand() % STATE_TRANS_RANGE;
    if (random_choice < cumu_trans_matrix[candle_state][0]) {
        candle_state = CANDLE_VERY_BRIGHT;
    } else if (random_choice < cumu_trans_matrix[candle_state][1]) {
        candle_state = CANDLE_BRIGHT;
    } else if (random_choice < cumu_trans_matrix[candle_state][2]) {
        candle_state = CANDLE_DIM;
    } else {
        candle_state = CANDLE_VERY_DIM;
    }

    int dwell_time = DWELL_TIM_MIN + rand() % (DWELL_TIM_MAX - DWELL_TIM_MIN + 1);
    HAL_Delay(dwell_time);
}
