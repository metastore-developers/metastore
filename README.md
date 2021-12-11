<p align="left">
    <a href="https://github.com/metastore-developers/metastore" title="Metastore">
        <img src="docs/_static/images/logo.svg" width="128px"/>
    </a>
</p>

[![Releases](https://img.shields.io/github/v/release/metastore-developers/metastore?color=blue)](https://github.com/metastore-developers/metastore/releases)
[![Issues](https://img.shields.io/github/issues/metastore-developers/metastore?color=blue)](https://github.com/metastore-developers/metastore/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/metastore-developers/metastore?color=blue)](https://github.com/metastore-developers/metastore/pulls)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://metastore.readthedocs.io)
[![License](https://img.shields.io/pypi/l/metastore?color=blue)](LICENSE.md)

# Metastore

Metastore Python SDK.

Feature store and data catalog for machine learning.

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
sphinx-build -b html . build/
```

## Changelog

[Changelog](CHANGELOG.md) contains information about new features, improvements, known issues, and bug fixes in each release.

## Copyright and license

Copyright (c) 2022, Metastore Developers. All rights reserved.

Project developed under a [BSD-3-Clause License](LICENSE.md).
