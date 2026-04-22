#include <stdint.h>

// Write a C function to calculate the sum of the negative elements of an
// array. Do not use any existing functions.

int32_t task2_func_c(int *arr, int n) {
    int32_t sum = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] < 0) {
            sum += arr[i];
        }
    }
    return sum;
}
