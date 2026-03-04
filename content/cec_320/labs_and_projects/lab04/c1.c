#include <stdint.h>
#include <stdio.h>
#include "main.h"
#include "de5d_logic_analyzer_fns.h"

static uint32_t mask_Pin0 =  0x0001U;  // 1U << 0
static uint32_t mask_Pin8 =  0x0100U;  // 1U << 8
static uint32_t mask_Pin10 = 0x0400U;  // 1U << 10

static uint32_t Pin0_pos = 0;
static uint32_t Pin8_pos = 8;
static uint32_t Pin10_pos = 10;

static uint8_t logic_samples[SAMPLES];
static uint32_t sample_delay = 100; // ms

// Initialization functions for GPIO pins:
void mp_Fnc6_init(void) {
    // MODER: PA0 = input, value = 0b00:
    GPIOA->MODER &= ~(3U << 0 * 2);

    // OTYPER: N/A
    // OSPEEDR: N/A

    // PUPDR: PA0 = pull-down, value = 0b10
    GPIOA->PUPDR &= ~(3U << 0 * 2);
    GPIOA->PUPDR |= (2U << 0 * 2);
}

void mp_LED1_init(void) {
    // MODER: PA10 = output, value = 0b01:
    GPIOA->MODER &= ~(3U << 10 * 2);
    GPIOA->MODER |= (1U << 10 * 2);

    // OTYPER: PA10 = push-pull, value = 0b0, which is default. Use default.

    // OSPEEDR: Use default
    // PUPDR: Use default
}

void mp_init_set_LED1_reset_LED4(void) {
    // LED1 = PA10: turn ON (set bit) using BSRR lower half
    GPIOA->BSRR = mask_Pin10;
    // LED4 = PB8: turn OFF (reset bit) using BSRR upper half
    GPIOB->BSRR = mask_Pin8 << 16;
}


// Other functions:

void mp_toggle_LEDs(void) {
    GPIOA->ODR ^= mask_Pin10;
    GPIOB->ODR ^= mask_Pin8;
}

void mp_read_logic_samples(void) {
    for (int i = 0; i < SAMPLES; i++) {
        uint8_t bit0 = (GPIOA->IDR >> Pin0_pos) & 1;   // CH1: PA0 via IDR
        uint8_t bit1 = (GPIOA->ODR >> Pin10_pos) & 1;   // CH2: PA10 via ODR
        uint8_t bit2 = (GPIOB->ODR >> Pin8_pos) & 1;    // CH3: PB8 via ODR
        logic_samples[i] = (bit2 << 2) | (bit1 << 1) | bit0;
        HAL_Delay(sample_delay);
    }
}

void mp_print_logic_samples(void) {
    printf("Sampling data for you...just a moment.\n");
    for (int ch = 0; ch < CHANNELS; ch++) {
        printf("CH%d: ", ch + 1);
        for (int j = 0; j < SAMPLES; j++) {
            printf("%d", (logic_samples[j] >> ch) & 1);
        }
        printf("\n");
    }
}
