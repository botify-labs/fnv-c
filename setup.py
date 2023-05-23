from setuptools import find_packages, setup

setup(
    name="fnv0",
    version="0.1.0",
    description="FIXME",
    long_description="FIXME",
    url="https://github.com/botify-labs/fnv-c",
    author="Fabien MARTY",
    author_email="fabien.marty@botify.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: MIT License",
    ],
    packages=find_packages(),
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["./fnv0/ext/build.py:ffibuilder"],
)
