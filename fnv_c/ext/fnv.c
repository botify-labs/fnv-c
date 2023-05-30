#include "fnv.h"

#define FNV_32_PRIME 0x01000193
#define FNV_64_PRIME 0x100000001b3
#define FNV1_32_INIT 0x811c9dc5
#define FNV1_64_INIT 0xcbf29ce484222325

uint32_t _fnv_32(void *data, size_t len, uint32_t hval_init, uint32_t fnv_prime, int aversion)
{
    uint32_t hval = hval_init;
    uint8_t *pointer = (uint8_t *) data;
    uint8_t *buf_end = pointer + len;
    while (pointer < buf_end) {
	if (aversion == 1) {
            hval ^= (uint32_t) *pointer++;
            hval *= fnv_prime;
	} else {
            hval *= fnv_prime;
            hval ^= (uint32_t) *pointer++;
	}
    }
    return hval;
}

uint64_t _fnv_64(void *data, size_t len, uint64_t hval_init, uint64_t fnv_prime, int aversion)
{
    uint64_t hval = hval_init;
    uint8_t *pointer = (uint8_t *) data;
    uint8_t *buf_end = pointer + len;
    while (pointer < buf_end) {
	if (aversion == 1) {
            hval ^= (uint64_t) *pointer++;
            hval *= fnv_prime;
	} else {
            hval *= fnv_prime;
            hval ^= (uint64_t) *pointer++;
	}
    }
    return hval;
}

uint32_t fnv0_32(void *data, size_t len)
{
    return _fnv_32(data, len, 0, FNV_32_PRIME, 0);
}

uint64_t fnv0_64(void *data, size_t len)
{
    return _fnv_64(data, len, 0, FNV_64_PRIME, 0);
}

uint32_t fnv1_32(void *data, size_t len)
{
    return _fnv_32(data, len, FNV1_32_INIT, FNV_32_PRIME, 0);
}

uint64_t fnv1_64(void *data, size_t len)
{
    return _fnv_64(data, len, FNV1_64_INIT, FNV_64_PRIME, 0);
}

uint32_t fnv1a_32(void *data, size_t len)
{
    return _fnv_32(data, len, FNV1_32_INIT, FNV_32_PRIME, 1);
}

uint64_t fnv1a_64(void *data, size_t len)
{
    return _fnv_64(data, len, FNV1_64_INIT, FNV_64_PRIME, 1);
}

