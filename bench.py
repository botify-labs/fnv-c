import platform
import timeit

BENCH_PYHASH = True
BENCH_FNVHASH = True

SIZES = (1, 5, 10, 50, 100, 500, 1000)

if BENCH_PYHASH and platform.machine() == "arm64":
    print("WARNING: pyhash is not compatible with ARM64")
    BENCH_PYHASH = False

if BENCH_FNVHASH:
    try:
        pass
    except ImportError:
        print("WARNING: fnvhash is not installed")
        print("=> do 'pip install fnvhash'")
        BENCH_FNVHASH = False

if BENCH_PYHASH:
    try:
        pass
    except ImportError:
        print("WARNING: pyhash is not installed")
        print("=> do 'pip install pyhash'")
        BENCH_PYHASH = False


def bench(imprt, hasher):
    setup = (
        """
import """
        + imprt
        + """
from random import randbytes

b = randbytes("""
        + str(size)
        + """)
hasher = """
        + imprt
        + "."
        + hasher
        + """
"""
    )
    return timeit.timeit(stmt="hasher(b)", setup=setup)


for size in SIZES:
    print(f">>> Benchmarking (1M times) on bytes of size {size}...")
    print("")
    print("fnv0_64 (fnv-c)   ", bench("fnv_c", "fnv0_64"))
    if BENCH_PYHASH:
        print("fnv0_64 (pyhash)  ", bench("pyhash", "fnv1_64()"))
    if BENCH_FNVHASH:
        print("fnv0_64 (fnvhash) ", bench("fnvhash", "fnv0_64"))
    print("")
    print("")
