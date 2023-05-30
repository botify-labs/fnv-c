#include <stdint.h>
#include <string.h>

uint32_t fnv0_32(void *data, size_t len);
uint64_t fnv0_64(void *data, size_t len);
uint32_t fnv1_32(void *data, size_t len);
uint64_t fnv1_64(void *data, size_t len);
uint32_t fnv1a_32(void *data, size_t len);
uint64_t fnv1a_64(void *data, size_t len);
