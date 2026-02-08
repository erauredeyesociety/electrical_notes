/* ce5d_debug_fib_app.c - Final code with PT 1, PT 2, and DT 6 bug fix */

#include <stdlib.h>
#include "mp_supported_mcu.h"
#include "mp_uart_redirect.h"
#include "mp_bin_str_printing.h"

static uint32_t fibonacci_arr1[11], fibonacci_arr2[14];

static int mp_update_fib_array(uint32_t *fib_arr, int N) {
    int ret_val = 0;   // return value: 0 = success
    if (N < 0) {
        ret_val = -1;
    } else if (N == 0) {
        fib_arr[0] = 0;
    } else if (N == 1) {
        fib_arr[0] = 0;
        fib_arr[1] = 1;
    } else if (N <= 20) {
        /* PT 1: Fibonacci computation from index 2 through N */
        fib_arr[0] = 0;
        fib_arr[1] = 1;
        int i = 2;
        while (i <= N) {
            fib_arr[i] = fib_arr[i-1] + fib_arr[i-2];
            i = i + 1;
        }
    } else {
        ret_val = -2;
    }
    return ret_val;
}

__attribute__((weak))
void mp_app(void) {
    printf("\n\nRunning ce5d_debug_fib App ---\n");

    char result_info[] =
            "Fibonacci number %2d: %4d \t %s \t 0X%02X\n";
    char bin_str[50];
    int dec_int = 0;
    int N[] = {-1, 0, 1, 5, 21};

    for (int i = 0; i < sizeof(N)/sizeof(N[0]); i++) {
        int call_status = mp_update_fib_array(fibonacci_arr1, N[i]);
        printf("Status of calling mp_update_fib_array with N=%d is %d\n",
                N[i], call_status);
    }

    mp_update_fib_array(fibonacci_arr1, 5);
    printf("\n--- 5 Fibonacci numbers from array 1: ---\n");
    for (int i = 1; i <= 5; i++) {
        dec_int = fibonacci_arr1[i];
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
    }

    mp_update_fib_array(fibonacci_arr1, 10);
    mp_update_fib_array(fibonacci_arr2, 13);

    /* PT 2: Print Fibonacci numbers from both arrays */
    printf("\n--- Fibonacci numbers from array 1: ---\n");
    for (int i = 1; i <= 10; i++) {
        dec_int = fibonacci_arr1[i];
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
    }

    printf("\n--- Fibonacci numbers from array 2: ---\n");
    for (int i = 1; i <= 13; i++) {
        dec_int = fibonacci_arr2[i];
        mp_bin_num_2_n_bit_vrbs_bin_str(bin_str, dec_int, 8);
        printf(result_info, i, dec_int, bin_str, dec_int);
    }

    while (1) {
    }
}
