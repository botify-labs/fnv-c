from fnv_c.ext._fnv import lib


def fnv0_64(data: bytes) -> int:
    return lib.fnv0_64(data, len(data))


def fnv0_32(data: bytes) -> int:
    return lib.fnv0_32(data, len(data))
