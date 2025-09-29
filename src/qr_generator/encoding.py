from bitarray import bitarray
from bitarray.util import int2ba

from .types import Mode
from .tables import _get_char_count_bits

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
