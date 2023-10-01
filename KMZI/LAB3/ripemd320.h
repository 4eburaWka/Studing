#ifndef _TEST_H_
#define _TEST_H_

#ifdef  __cplusplus
extern "C" {
#endif

#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

uint32_t f(int j, uint32_t x, uint32_t y, uint32_t z);
uint32_t K1(int j);
uint32_t K2(int j);
char *ripemd320(const char *message);

#ifdef  __cplusplus
}
#endif

#endif  /* _TEST_H_ */