from setuptools import setup

# Bumped at release time by `invoke bump-version` (dunamai). Wired into the
# package metadata via `dynamic = ["version"]` in pyproject.toml.
VERSION = "0.0.0"


setup(
    version=VERSION,
    cffi_modules=["./fnv_c/ext/build.py:ffibuilder"],
)
