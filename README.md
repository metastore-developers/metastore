# Metastore

Metastore Python SDK.

## Prerequisites

* [Python (>=3.7.0)](https://www.python.org)

## Installation

### Production

Install package:

```
pip install metastore
```

### Development

Install package:

```
pip install -e .[development]
```

> **Note** Use the `-e, --editable` flag to install the package in development mode.

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
sphinx-build -b html source/ build/
```

## Changelog

[Changelog](CHANGELOG.md) contains information about new features, improvements, known issues, and bug fixes in each release.

## Copyright and license

Copyright (c) 2022, Metastore Developers. All rights reserved.

Project developed under a [BSD-3-Clause License](LICENSE.md).
