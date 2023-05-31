from __future__ import annotations

from dunamai import Style, Version
from invoke import task

PACKAGE = "fnv_c"


def _clean_apidoc(c):
    c.run("rm -Rf apihtml")


def _clean_coverage(c):
    c.run("rm -Rf htmlcov")


@task
def clean(c):
    """Clean the repository"""
    c.run(f"rm -f {PACKAGE}/ext/*.o {PACKAGE}/ext/*.so {PACKAGE}/ext/_fnv*")
    c.run("rm -Rf *.egg-info .*_cache build ")
    c.run("find . -type d -name __pycache__ -exec rm -Rf {} \\; 2>/dev/null || true")
    c.run("rm -Rf dist build")
    _clean_apidoc(c)
    _clean_coverage(c)


@task(help={"fix": "try to automatically fix the code (default)"})
def lint_black(c, fix=True):
    """Lint the code with black"""
    if fix:
        c.run("black .")
    else:
        c.run("black --check .")


@task(help={"fix": "try to automatically fix the code (default)"})
def lint_ruff(c, fix=True):
    """Lint the code with ruff"""
    if fix:
        c.run("ruff . --fix")
    else:
        c.run("ruff .")


@task(help={"fix": "try to automatically fix the code (default)"})
def lint(c, fix=True):
    """Lint the code with all linters"""
    lint_ruff(c, fix=fix)
    lint_black(c, fix=fix)


@task(help={"coverage": "compute coverage"})
def test(c, coverage=False):
    """Execute unit tests"""
    if coverage:
        _clean_coverage(c)
        c.run(
            f"pytest --cov-config=.coveragerc --no-cov-on-fail --cov={PACKAGE} --cov-report=term --cov-report=html --cov-report=xml ."
        )
    else:
        c.run("pytest .")


@task
def apidoc(c):
    """Make API doc"""
    _clean_apidoc(c)
    c.run(f"pdoc3 --html --output-dir=apihtml {PACKAGE}")


@task
def bump_version(c, force_version: str | None = None):
    if force_version is None:
        version = Version.from_git().serialize(style=Style.SemVer)
    else:
        version = force_version

    print(f"Setting version={version}")

    with open("setup.py") as f:
        c = f.read()

    lines = []
    for line in c.splitlines():
        if line.startswith("VERSION = "):
            lines.append(f'VERSION = "{version}"')
        else:
            lines.append(line)

    with open("setup.py", "w") as g:
        g.write("\n".join(lines))
