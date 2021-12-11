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
autopep8 --recursive --in-place setup.py metastore/
```

Lint source code:

```
pylint setup.py metastore/
```

Test package:

```
pytest
```

Report test coverage:

```
pytest --cov
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
