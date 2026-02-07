Source code in the `proj1_src` folder used for Project 1:

`_mp_main.c`:

```c
void mp_main(void) {
#if defined(UNIT_TEST)
    void mp_unity(void);
    mp_unity();
#else
    void mp_app(void);
    mp_app();
#endif
}
```

`proj1_app.c`:

```c
#include <stdio.h>
#include "mp_supported_mcu.h"
#include "mp_uart_redirect.h"
#include "proj1_fns.h"

void mp_app(void) {
    printf("\nRunning Proj1 main App:\n");

    while (1);
}
```

`proj1_cfns.c`:

```c
void mp_swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}

void mp_partial_sum(int *arr, int arr_size, int *result) {

}

int mp_reverse_str(char *src, char *dst) {

}
```

`proj1_fns.h`:

```c
#pragma once

#ifdef __cplusplus
extern "C" {
#endif /* __cplusplus */

void mp_swap(int a, int b);
void mp_partial_sum(int *arr, int arr_size, int *result);
int mp_reverse_str(char *src, char *dst);

#ifdef __cplusplus
}
#endif /* __cplusplus */
```

Source code in the `proj1_test` folder used for Project 1:

`test_proj1.c`:

```c
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include "unity.h"
#include "proj1_fns.h"


void test_mp_swap(void) {
    int exp[] = {2, 1};
    int act[] = {1, 2};
    mp_swap(act[0], act[1]);
    TEST_ASSERT_EQUAL_INT_ARRAY(exp, act, 2);
}

void test_mp_partial_sum(void) {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int exp1[] = {1, 2};   // arr_size = 2
    int exp2[] = {9, 12};  // arr_size = 6
    int act1[2];
    int act2[2];

    mp_partial_sum(arr, 2, act1);
    mp_partial_sum(arr, 6, act2);

    TEST_ASSERT_EQUAL_INT_ARRAY(exp1, act1, 2);
    TEST_ASSERT_EQUAL_INT_ARRAY(exp2, act2, 2);
}

void test_mp_reverse_str(void) {

    TEST_ASSERT_TRUE(1 > 2);
}


void mp_unity(void) {
    printf("\nRunning Proj1 unit test:\n");

    UNITY_BEGIN();

    RUN_TEST(test_mp_swap);
    RUN_TEST(test_mp_partial_sum);
    RUN_TEST(test_mp_reverse_str);

    UNITY_END();

    while (1);
}
```
