void test_mp_reverse_str(void) {
    char src[] = "Hello.";
    char dst[7];
    char exp[] = ".olleH";

    int result = mp_reverse_str(src, dst);

    TEST_ASSERT_EQUAL_INT(6, result);
    TEST_ASSERT_EQUAL_UINT8_ARRAY(exp, dst, 7);
}
