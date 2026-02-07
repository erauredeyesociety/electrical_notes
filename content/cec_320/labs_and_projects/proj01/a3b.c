int mp_reverse_str(char *src, char *dst) {
    int len = 0;
    char *p = src;

    while (*p != '\0') {
        len++;
        p++;
    }

    for (int i = 0; i < len; i++) {
        dst[i] = src[len - 1 - i];
    }
    dst[len] = '\0';

    return len;
}
