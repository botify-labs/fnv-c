# Contributing

## Prerequisites

This project uses [uv](https://docs.astral.sh/uv/) to manage the dev
environment (it builds the C extension and installs the dev dependencies):

```
uv sync
```

## Linting, tests...

This project uses [Invoke](https://www.pyinvoke.org/) to launch various dev scripts.

For example, to execute linting:

```
uv run invoke lint
```

To get the list of all dev scripts

```
uv run invoke --list
```

## Releasing

The release process is completly automated in Github Action.

Just create a new GitHub release with the UI associated to a tag `vX.Y.Z` (don't miss the leading (lowercase) `v`).
