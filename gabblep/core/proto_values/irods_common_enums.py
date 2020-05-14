from enum import Enum


class AuthScheme(Enum):
    '''
        Enumeration of iRODS auth schemes
    '''
    STANDARD = 'STANDARD'
    GREEN = 'PAM'
