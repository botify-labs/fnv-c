from invoke import task

PACKAGE = "fnv_c"


def _clean_apidoc(c):
    c.run("rm -Rf apihtml")


@task
def clean(c):
    """Clean the repository"""
    c.run(f"rm -f {PACKAGE}/ext/*.o {PACKAGE}/ext/*.so {PACKAGE}/ext/_fnv*")
    c.run(
        "rm -Rf *.egg-info .*_cache build ; find . -type d -name __pycache__ -exec rm -Rf {} \\; 2>/dev/null"
    )
    c.run("rm -Rf dist build")
    _clean_apidoc(c)


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


@task()
def test(c, coverage=False):
    """Execute unit tests"""
    c.run("pytest .")


@task
def apidoc(c):
    """Make API doc"""
    _clean_apidoc(c)
    c.run(f"pdoc3 --html --output-dir=apihtml {PACKAGE}")
