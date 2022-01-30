'''
Secret configuration model.
'''

from typing import Literal

from .configuration import Configuration


class SecretConfiguration(Configuration):
    '''
    Secret configuration model.
    '''

    #: Configuration type.
    type: Literal['secret']
    #: Secret name.
    name: str


__all__ = [
    'SecretConfiguration'
]
