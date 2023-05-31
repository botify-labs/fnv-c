# fnv-c

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/botify-labs/fnv-c/lint.yaml)](https://github.com/botify-labs/fnv-c/actions/workflows/lint.yaml)
[![Codecov](https://img.shields.io/codecov/c/github/botify-labs/fnv-c)](https://app.codecov.io/github/botify-labs/fnv-c)
[![pypi badge](https://img.shields.io/pypi/v/fnv-c?color=brightgreen)](https://pypi.org/project/fnv-c/)

## What is it?

**fnv-c** is a Python 3.7+ FNV (`fnv0`, `fnv1`, `fnv1a`) **non-cryptographic** hash library implemented in C through libffi.

FNV ("Fowler–Noll–Vo") is is a non-cryptographic hash function created by Glenn Fowler, Landon Curt Noll, and Kiem-Phong.
FNV is probably no the "best" non-cryptographic hash function but:

- it has a reasonably good distribution
- it's very fast
- it's very easy to implement *(even in some exotic stored procedures for example)* so you can use it everywhere

More details on [this Wikepedia article](https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function).

## Features

- speed: **4 000%** faster than basic Python implementation, **40%** faster than `pyhash`
- portability:
    - tested with recent Python versions (3.7+)
    - compatible with ARM64
    - compatible with PyPy

## Non features

- other hash algorithms (this library is only about FNV algorithm)
- too agressive CPU optimizations (we prefer maximizing binary portability)

## How to install/use it?

```
pip install fnv-c
```

```python
import fnv_c

print(fnv_c.fnv0_32(b"foo bar"))
print(fnv_c.fnv0_64(b"foo bar"))
print(fnv_c.fnv1_32(b"foo bar"))
print(fnv_c.fnv1_64(b"foo bar"))
print(fnv_c.fnv1a_32(b"foo bar"))
print(fnv_c.fnv1a_64(b"foo bar"))
```

## Function signatures / API

Full API doc is available at: [https://botify-labs.github.io/fnv-c/fnv_c/](https://botify-labs.github.io/fnv-c/fnv_c/)

## Dev

See [this specific document](DEV.md)
