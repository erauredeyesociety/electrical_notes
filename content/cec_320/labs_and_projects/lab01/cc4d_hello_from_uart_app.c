#include <stdio.h>
#include "mp_supported_mcu.h"
#include "mp_uart_redirect.h"

static void mp_str2name(char *str, char *name);

void mp_app(void) {
    printf("Hello from UART!\n");

    SET_STDIN_TO_NO_BUFFER;
    char str[50];
    char name[50];
    while (1) {
        printf("Please input your name (with '~' for space): \n");
        scanf("%s", str);
        mp_str2name(str, name);
        printf("Hello %s.\n", name);
    }
}

static void mp_str2name(char *str, char *name) {
    char ch;
    do {
        ch = *str++;
        if (ch == '~') {
            *name++ = ' ';
        } else {
            *name++ = ch;
        }
    } while (ch);
}
