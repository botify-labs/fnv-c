from fnv_c.ext._fnv import lib

__pdoc__ = {"ext": False}


def fnv0_32(data: bytes) -> int:
    """Compute a FNV0 hash on given bytes and return an unsigned 32bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV0 HASH as an unsigned 32bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv0_32(data, len(data))


def fnv0_64(data: bytes) -> int:
    """Compute a FNV0 hash on given bytes and return an unsigned 64bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV0 HASH as an unsigned 64bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv0_64(data, len(data))


def fnv1_32(data: bytes) -> int:
    """Compute a FNV1 hash on given bytes and return an unsigned 32bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV1 HASH as an unsigned 32bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv1_32(data, len(data))


def fnv1_64(data: bytes) -> int:
    """Compute a FNV1 hash on given bytes and return an unsigned 64bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV1 HASH as an unsigned 64bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv1_64(data, len(data))


def fnv1a_32(data: bytes) -> int:
    """Compute a FNV1a hash on given bytes and return an unsigned 32bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV1a HASH as an unsigned 32bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv1a_32(data, len(data))


def fnv1a_64(data: bytes) -> int:
    """Compute a FNV1a hash on given bytes and return an unsigned 64bits integer.

    Args:
        data: the bytes to hash.

    Returns:
        The corresponding FNV1a HASH as an unsigned 64bits integer.

    """
    assert isinstance(data, bytes)
    return lib.fnv1a_64(data, len(data))
