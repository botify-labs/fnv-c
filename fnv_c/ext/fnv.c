#include "fnv.h"

uint64_t fnv0_64(void *data, size_t len)
{
    uint64_t hval = 0;
    uint8_t *pointer = (uint8_t *) data;
    uint8_t *buf_end = pointer + len;
    while (pointer < buf_end) {
        hval *= 0x100000001B3;
        hval ^= (uint64_t) *pointer++;
    }
    return hval;
}

uint32_t fnv0_32(void *data, size_t len)
{
    uint32_t hval = 0;
    uint8_t *pointer = (uint8_t *) data;
    uint8_t *buf_end = pointer + len;
    while (pointer < buf_end) {
	hval *= 0x01000193;
	hval ^= (uint64_t) *pointer++;
    }
    return hval;
}
