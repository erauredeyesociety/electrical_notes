void test_mp_gpio_toggle_pins_func(void) {
    uint32_t act, exp = 0xABCD, odr = 0xAB3D;
    GPIOx->ODR = odr;
    mp_GPIO_TogglePinS(GPIOx, (15U<<4));
    act = mp_mock_read_odr(GPIOx);
    TEST_ASSERT_EQUAL_UINT32(exp, act);
}
