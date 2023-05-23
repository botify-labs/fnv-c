# fnv0

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/botify-labs/fnv-c/lint.yaml)](https://github.com/botify-labs/fnv-c/actions/workflows/lint.yaml)

## What is it?

Python 3.7+ is a FNV0 hash library implemented in C through libffi.

## Features

- speed: **4 000%** faster than basic Python implementation, **40%** faster than `pyhash`
- portability:
    - tested with recent Python versions (3.7+)
    - compatible with ARM64 and avoid too agressive CPU optimizations
    - compatible with PyPy
- two variants: 32bits (`fnv0_32()`) and 64bits (`fnv0_64()`)

## Non features

- other hash algorithms (this library is about a specific algorithm)

## How to install/use it?

```
pip install git+https://github.com/botify-labs/fnv-c.git#egg=fnv0
```

```python
import fnv0

print(fnv0.fnv0_32(b"foo bar"))
print(fnv0.fnv0_64(b"foo bar"))
```

## Function signatures / API

```
fnv0_32(data: bytes) -> int
fnv0_64(data: bytes) -> int
```

## Dev

```
pip install -r dev-requirements.txt
python setup.py develop

# get all tasks (lint, test, clean...)
invoke --list
```
