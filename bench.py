import timeit

SIZES = (1, 10, 100, 1000)
STMTS = ("fnv0_32", "fnv0_64", "fnv1_32", "fnv1_64", "fnv1a_32", "fnv1a_64")

TOBENCHS = [
    {
        "project": "fnv_c",
        "import": "fnv_c",
    },
    {
        "project": "fnvhash",
        "import": "fnvhash",
    },
]


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


for stmt in STMTS:
    for size in SIZES:
        print(f">>> Benchmarking (1M times) {stmt} on bytes of size {size}...")
        print("")
        for tobench in TOBENCHS:
            print(f"{tobench['project']:10}", bench(tobench["import"], stmt))
        print("")
        print("")
