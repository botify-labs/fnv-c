# DEV

## Prerequisites

```
pip install -r dev-requirements.txt
```

## Linting, tests...

This project uses [Invoke](https://www.pyinvoke.org/) to launch various dev scripts.

For example, to execute linting:

```
invoke lint
```

To get the list of all dev scripts

```
invoke --list
```

## Releasing

The release process is completly automated in Github Action.

Just create a new GitHub release with the UI associated to a tag `vX.Y.Z` (don't miss the leading (lowercase) `v`).

