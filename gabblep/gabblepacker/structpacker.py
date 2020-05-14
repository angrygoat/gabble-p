import struct
import logging
from ..gabbleutils import gabble_logging_config

"""

structpacker is a set of functions that can translate iRODS protocol messages into packed record formats that
can be transmitted to iRODS, and can read responses from iRODS and turn them into python data structures

"""

gabble_logging_config.setup_logging()
logger = logging.getLogger(__name__)


def pack_MsgHeader_PI(type, msglen, errorlen, bslen, intinfo):
    """
    
    :param type:
    :param msglen:
    :param errorlen:
    :param bslen:
    :param intinfo:
    :return:
    """