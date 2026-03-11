void mp_hp_ieee754_encoding(float f, hp_IEEE754Field_TypeDef *pField) {
    const double hp_float_max = pow(2.0, bias+1) - pow(2.0, bias-n_frac);
    const double hp_float_min_norm = pow(2.0, (1-bias));

    // Determine pField->sign
    if (f < 0) {
        pField->sign = 1;
        f = -f;
    } else {
        pField->sign = 0;
    }

    double fabs_val = (double)f;

    // The following will be executed only if f is not bigger than the max.
    if (fabs_val > hp_float_max) {
        // Too big: represent as infinity (exponent all 1s, fraction 0)
        pField->exponent = (1 << n_expt) - 1;  // 31
        pField->fraction = 0;
        return;
    }

    // Determine pField->exponent and pField->fraction
    if (fabs_val >= hp_float_min_norm) {
        // Normal number
        int exponent = (int)floor(log2(fabs_val));
        pField->exponent = exponent + bias;
        double mantissa = fabs_val / pow(2.0, exponent) - 1.0;
        pField->fraction = (uint16_t)(mantissa * pow(2.0, n_frac) + 0.5);
    } else {
        // Denormalized number (or zero)
        pField->exponent = 0;
        pField->fraction = (uint16_t)(fabs_val / pow(2.0, 1 - bias) * pow(2.0, n_frac) + 0.5);
    }

    return;
}

float mp_hp_ieee754_decoding(hp_IEEE754Field_TypeDef field) {
    float decoded = 0.0;

    if (field.exponent == ((1 << n_expt) - 1)) {
        // Exponent all 1s: infinity or NaN
        if (field.fraction == 0) {
            decoded = (float)pow(2.0, 128);  // large value representing infinity
        } else {
            decoded = 0.0f / 0.0f;  // NaN
        }
    } else if (field.exponent == 0) {
        // Denormalized number (or zero)
        decoded = (float)((double)field.fraction / pow(2.0, n_frac) * pow(2.0, 1 - bias));
    } else {
        // Normal number
        decoded = (float)((1.0 + (double)field.fraction / pow(2.0, n_frac))
                          * pow(2.0, field.exponent - bias));
    }

    if (field.sign) {
        decoded = -decoded;
    }

    return decoded;
}
