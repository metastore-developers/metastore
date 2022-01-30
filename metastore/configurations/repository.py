'''
Repository configuration model.
'''

from typing import Dict, List, Literal, Optional

from .. import types
from .configuration import Configuration


class RepositoryConfiguration(Configuration):
    '''
    Repository configuration model.
    '''

    #: Configuration type.
    type: Optional[Literal['repository']] = 'repository'
    #: Project name.
    name: str
    #: Project display name.
    display_name: Optional[str] = None
    #: Project description.
    description: Optional[str] = None
    #: Project author name.
    author: Optional[str] = None
    #: Project tags.
    tags: Optional[List[Dict[str, str]]] = None
    #: Project version.
    version: str
    #: Credential store configurations.
    credential_store: Optional[types.CredentialStore] = None
    #: Metadata store configurations.
    metadata_store: types.MetadataStore
    #: Offline store configurations.
    offline_store: types.OfflineStore
    #: Online store configurations.
    online_store: types.OnlineStore
    #: Data source configurations.
    data_sources: Optional[List[types.DataSource]] = None


__all__ = [
    'RepositoryConfiguration'
]
