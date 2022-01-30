# Contributing

## Prerequisites

* [Python (>=3.8.0)](https://www.python.org)

## Development

Install package:

```console
pip install -e .[development]
```

```{note}
Use the `-e, --editable` flag to install the package in development mode.
```

```{note}
Set up a virtual environment for development.
```

Format source code:

```console
autopep8 --recursive --in-place setup.py metastore/ tests/
```

Lint source code:

```console
pylint setup.py metastore/ tests/
```

Test package:

```console
pytest
```

Report test coverage:

```console
pytest --cov --cov-fail-under 80
```

```{note}
Set the `--cov-fail-under` flag to 80% to validate the code coverage metric.
```

Build documentation:

```console
cd docs/
sphinx-build -b html metastore/ build/
```

```{note}
This step will generate the API reference before building.
```
