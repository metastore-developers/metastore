'''
Pygments styles.
'''

from pygments.style import Style
from pygments.token import (
    Comment,
    Operator,
    Name,
    Keyword,
    String,
    Literal,
    Number,
    Error
)


class MetastoreStyle(Style):
    '''
    Metastore syntax highlighting style.
    '''

    default_style = ''

    styles = {
        Comment: '#666f78',
        Comment.Preproc: '#666f78',
        Operator: '#000000',
        Name: '#000000',
        Name.Builtin: 'bold #015493',
        Name.Builtin.Pseudo: 'bold #015493',
        Name.Variable: '#000000',
        Name.Tag: 'bold #015493',
        Name.Decorator: '#000000',
        Name.Label: '#000000',
        Name.Attribute: '#000000',
        Name.Class: '#000000',
        Name.Function: '#000000',
        Keyword: 'bold #015493',
        String: '#dd2458',
        String.Char: '#dd2458',
        Literal: '#009b44',
        Number: '#009b44',
        Error: '#000000'
    }
