'''
Sphinx configuration file.
'''

import os
import sys
from typing import Any, Tuple, Dict

sys.path.append(os.path.abspath('_pygments/'))

from sphinx.application import Sphinx
from sphinx.ext import apidoc

import metastore


def generate_documentation(*args: Tuple[Any], **kwargs: Dict[str, Any]):
    '''
    Generate API reference documentation.

    Parameters:
        *args (Tuple[Any]): Additional arguments.
        **kwargs (Dict[str, Any]): Additional keyword arguments.
    '''

    module = os.path.abspath('../metastore/')
    output = os.path.abspath('metastore/api-reference/')

    apidoc.main(['-f', '-e', '-T', '-d', '2', '-o', output, module])


def setup(app: Sphinx):
    '''
    Sphinx setup stage.

    Parameters:
        app (Sphinx): Sphinx application instance.
    '''

    app.connect('builder-inited', generate_documentation)


project = metastore.__title__
version = metastore.__version__
author = metastore.__author__
copyright = metastore.__copyright__[:-1]

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser'
]

autodoc_default_options = {
    'special-members': True
}

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}
exclude_patterns = [
    'build'
]

html_theme = 'pydata_sphinx_theme'

html_static_path = [
    '_static'
]
html_css_files = [
    'styles/custom.css'
]
templates_path = [
    '_templates'
]

html_title = f'{project} Documentation'
html_favicon = '_static/images/favicon.ico'
html_logo = '_static/images/logo.svg'

html_theme_options = {
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/metastore-developers/metastore',
            'icon': 'fab fa-github'
        },
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/metastore',
            'icon': 'fab fa-python'
        }
    ]
}

pygments_style = 'style.MetastoreStyle'
