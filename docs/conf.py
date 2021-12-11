import metastore


project = metastore.__title__
version = metastore.__version__
author = metastore.__author__
copyright = metastore.__copyright__[:-1]

extensions = [
    'sphinx.ext.autodoc',
    'myst_parser'
]
source_suffix = {
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
