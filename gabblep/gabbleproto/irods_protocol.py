import logging
from src.gabbleutils import gabble_logging_config
from twisted.internet.protocol import Protocol

from twisted.internet import ssl, task, protocol, endpoints, defer
from twisted.python.modules import getModule



"""

irods_protocol is a twisted protocol implementation that handles iRODS client connections

see: https://twistedmatrix.com/documents/current/core/howto/clients.html


"""

gabble_logging_config.setup_logging()


class IrodsProtocol(Protocol):
    pass