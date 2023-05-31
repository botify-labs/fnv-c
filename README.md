# fnv-c

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/botify-labs/fnv-c/lint.yaml)](https://github.com/botify-labs/fnv-c/actions/workflows/lint.yaml)

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
    - compatible with ARM64 and avoid too agressive CPU optimizations for maximizing binary portability 
    - compatible with PyPy

## Non features

- other hash algorithms (this library is about a specific algorithm)

## How to install/use it?

```
pip install fnv-c
```

```python
import fnv_c

print(fnv_c.fnv0_32(b"foo bar"))
print(fnv_c.fnv0_64(b"foo bar"))
```

## Function signatures / API

Full API doc is available at: [https://botify-labs.github.io/fnv-c/fnv_c/](https://botify-labs.github.io/fnv-c/fnv_c/)

## Dev

```
pip install -r dev-requirements.txt
python setup.py develop

# get all tasks (lint, test, clean...)
invoke --list
```
