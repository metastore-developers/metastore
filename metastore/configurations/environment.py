'''
Environment configuration model.
'''

from typing import Literal

from .configuration import Configuration


class EnvironmentConfiguration(Configuration):
    '''
    Environment configuration model.
    '''

    #: Configuration type.
    type: Literal['environment']
    #: Environment variable name.
    name: str


__all__ = [
    'EnvironmentConfiguration'
]
