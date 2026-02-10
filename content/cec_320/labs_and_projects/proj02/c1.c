void mp_mock_write_idr(GPIO_TypeDef *GPIOx, uint32_t idr) {
    GPIOx->IDR = idr;
}
