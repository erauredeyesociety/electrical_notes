#include "ci1s_ptr_funs.h"

void mp_strcpy(char *dst, char *src) {
    int i = 0;
    char ch = src[i];
    while (ch) {
        dst[i] = ch;
        i++;
        ch = src[i];
    }
    dst[i] = '\0';
}
