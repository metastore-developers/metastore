'''
Python setup script.
'''

import os
from typing import Dict
from distutils.util import convert_path
from setuptools import setup, find_packages


def get_package_info(path: str) -> Dict[str, str]:
    '''
    Get package description information.

    Parameters:
        path (str): Path to directory defining package main module.
    Returns:
        Dict[str, str]: A dictionary containing package information.
    '''

    with open(
        convert_path(os.path.join(path, 'package.py')),
        encoding='utf-8'
    ) as file:
        package_dict = {}
        exec(file.read(), package_dict)  # pylint: disable=W0122

        return package_dict


def parse_long_description() -> str:
    '''
    Get package long description.

    Returns:
        str: A string representing package long description.
    '''

    with open(convert_path('README.md'), encoding='utf-8') as file:
        return file.read()


PACKAGE_NAME = 'metastore'

package_info = get_package_info(PACKAGE_NAME)

vault_requirements = [
    'hvac>=0.11.0'
]

openmetadata_requirements = [
    'openmetadata-ingestion>=0.5.0'
]

postgresql_requirements = [
    'sqlalchemy>=1.4.20',
    'psycopg2>=2.9.0'
]

teradata_requirements = [
    'sqlalchemy>=1.4.20',
    'teradatasqlalchemy>=17.0.0'
]

s3_requirements = [
    's3fs>=2021.11.0'
]

redis_requirements = [
    'redis>=4.1.0'
]

all_requirements = [
    *vault_requirements,
    *openmetadata_requirements,
    *postgresql_requirements,
    *teradata_requirements,
    *s3_requirements,
    *redis_requirements
]

setup(
    name=PACKAGE_NAME,
    version=package_info['__version__'],
    description=package_info['__description__'],
    long_description=parse_long_description(),
    long_description_content_type='text/markdown',
    author=package_info['__author__'],
    author_email=package_info['__email__'],
    license=package_info['__license__'],
    url='https://metastore.readthedocs.io',
    download_url='https://pypi.org/project/metastore',
    project_urls={
        'Code': 'https://github.com/metastore-developers/metastore',
        'Issue tracker': 'https://github.com/metastore-developers/metastore/issues'
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License'
    ],
    python_requires='>=3.7.0',
    install_requires=[
        'python-dotenv>=0.19.0',
        'pydantic>=1.9.0',
        'dask>=2021.11.0'
    ],
    extras_require={
        'vault': vault_requirements,
        'openmetadata': openmetadata_requirements,
        'postgresql': postgresql_requirements,
        'teradata': teradata_requirements,
        's3': s3_requirements,
        'redis': redis_requirements,
        'all': all_requirements,
        'development': [
            *all_requirements,
            'setuptools>=58.2.0',
            'wheel>=0.37.0',
            'autopep8>=1.6.0',
            'pylint>=2.12.0',
            'pytest>=6.2.0',
            'pytest-cov>=3.0.0',
            'sphinx>=4.3.0',
            'myst-parser>=0.15.0',
            'pydata-sphinx-theme>=0.7.0',
            'twine>=3.7.0',
            'bump2version>=1.0.0'
        ]
    },
    packages=find_packages(),
    package_data={
        PACKAGE_NAME: [
            '../README.md',
            '../CHANGELOG.md',
            '../LICENSE.md'
        ]
    },
    zip_safe=False
)
