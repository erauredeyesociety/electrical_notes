void mp_partial_sum(int *arr, int arr_size, int *result) {
    result[0] = 0;
    result[1] = 0;

    for (int i = 0; i < arr_size; i++) {
        if (i % 2 == 0) {
            result[0] += *(arr + i);
        } else {
            result[1] += arr[i];
        }
    }
}
