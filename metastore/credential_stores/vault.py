'''
HashiCorp Vault credential store object.
'''

from .credential_store import CredentialStore


class VaultCredentialStore(CredentialStore):
    '''
    HashiCorp Vault credential store object.
    '''

    pass


__all__ = [
    'VaultCredentialStore'
]
