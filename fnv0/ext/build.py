from cffi import FFI

ffibuilder = FFI()

ffibuilder.cdef(
    """
    uint64_t fnv0_64(void *data, size_t len);
    uint32_t fnv0_32(void *data, size_t len);
"""
)
ffibuilder.set_source(
    "fnv0.ext._fnv0",
    """
    #include <stdint.h>
    #include <string.h>

    uint64_t fnv0_64(void *data, size_t len);
    uint32_t fnv0_32(void *data, size_t len);
""",
    sources=["fnv0/ext/fnv0.c"],
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
