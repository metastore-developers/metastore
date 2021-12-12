# Contributing

## Prerequisites

* [Python (>=3.7.0)](https://www.python.org)

## Development

Install package:

```
pip install -e .[development]
```

```{note}
Use the `-e, --editable` flag to install the package in development mode.
```

Format source code:

```
autopep8 --recursive --in-place setup.py metastore/ tests/
```

Lint source code:

```
pylint setup.py metastore/ tests/
```

Test package:

```
pytest
```

Report test coverage:

```
pytest --cov --cov-fail-under 80
```

```{note}
Set the `--cov-fail-under` flag to 80% to validate the code coverage metric.
```

Build package:

```
python setup.py bdist_wheel
```

Publish package:

```
twine upload dist/*
```

Build documentation:

```
cd docs/
sphinx-build -b html . build/
```
