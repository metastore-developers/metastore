'''
Value type enumeration.
'''

from enum import Enum


class ValueType(Enum):
    '''
    Value type enumeration.
    '''

    #: Integer value type.
    INTEGER = 'integer'
    #: Fractional (decimal numbers) value type.
    FRACTIONAL = 'fractional'
    #: String value type.
    STRING = 'string'


__all__ = [
    'ValueType'
]
