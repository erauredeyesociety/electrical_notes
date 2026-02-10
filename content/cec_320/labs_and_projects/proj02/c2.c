void mp_mock_odr_update_with_bsrr(GPIO_TypeDef *GPIOx) {
    if (GPIOx->BSRR != 0) {
        GPIOx->ODR |= (GPIOx->BSRR & 0xFFFF);
        GPIOx->ODR &= ~(GPIOx->BSRR >> 16);
        GPIOx->BSRR = 0;
    }
}
