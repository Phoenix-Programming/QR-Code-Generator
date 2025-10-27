from bitarray import bitarray
from bitarray.util import int2ba

from .types import Mode
from .tables import _get_char_count_bits, _ALPHANUMERIC_CHARACTER_TABLE

def _encode_numeric(data: str, version: int) -> bitarray:
    """
    Encodes numeric data for a QR code. Does NOT handle padding the data to the correct length. 

    Assumes input data is already confirmed to be numeric. 
    """
    character_count = len(data)
    encoded_data = bitarray()

    # add mode info
    encoded_data += int2ba(Mode.NUMERIC, 4)

    # number of bits used depends on qr version (size)
    character_count_bits = _get_char_count_bits(Mode.NUMERIC, version)
    encoded_data += int2ba(character_count, character_count_bits)

    # break into substrings of length <=3
    for i in range(0, character_count, 3):
        sub_str = data[i:i+3]

        # 10 bits for len = 3, 7 bits for len = 2, 4 bits for len = 1
        encoded_data += int2ba(int(sub_str), 3*len(sub_str) + 1)


    return encoded_data

def _encode_alphanumeric(data: str, version: int) -> bitarray:
    """
    Encodes alphanumeric data for a QR code. Does not handle padding the data to the correct length.

    Assumes input data is already confirmed to be alphanumeric.
    """
    character_count = len(data)
    encoded_data = bitarray()

    # add mode info
    encoded_data += int2ba(Mode.ALPHANUMERIC, 4)

    # number of bits used depends on qr version (size)
    character_count_bits = _get_char_count_bits(Mode.ALPHANUMERIC, version)
    encoded_data += int2ba(character_count, character_count_bits)

    # break into pairs of characters
    # iterator starts at 1 so the last character is skipped when the data length is odd
    for i in range(1, character_count, 2):
        numeric = (45 * _ALPHANUMERIC_CHARACTER_TABLE[data[i - 1]]) + _ALPHANUMERIC_CHARACTER_TABLE[data[i]]
        encoded_data += int2ba(numeric, 11)
    if (character_count & 1) == 1:
        encoded_data += int2ba(_ALPHANUMERIC_CHARACTER_TABLE[data[-1]], 6)

    return encoded_data
