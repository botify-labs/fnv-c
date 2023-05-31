from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """
    uint64_t fnv0_64(void *data, size_t len);
    uint32_t fnv0_32(void *data, size_t len);
    uint64_t fnv1_64(void *data, size_t len);
    uint32_t fnv1_32(void *data, size_t len);
    uint64_t fnv1a_64(void *data, size_t len);
    uint32_t fnv1a_32(void *data, size_t len);
"""
)
ffibuilder.set_source(
    "fnv_c.ext._fnv",
    """
    #include <stdint.h>
    #include <string.h>

    uint64_t fnv0_64(void *data, size_t len);
    uint32_t fnv0_32(void *data, size_t len);
    uint64_t fnv1_64(void *data, size_t len);
    uint32_t fnv1_32(void *data, size_t len);
    uint64_t fnv1a_64(void *data, size_t len);
    uint32_t fnv1a_32(void *data, size_t len);
""",
    sources=["fnv_c/ext/fnv.c"],
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
