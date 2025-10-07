from . import types

# alphanumeric characters are not encoded with unicode and instead use a special table
_ALPHANUMERIC_CHARACTER_TABLE = {
    " ": 36, "$": 37, "%": 38,
    "*": 39, "+": 40, "-": 41,
    ".": 42, "/": 43, ":": 44
}
for i in range(ord("0"), ord("9") + 1):
    _ALPHANUMERIC_CHARACTER_TABLE[chr(i)] = i - ord("0")
for i in range(ord("A"), ord("Z") + 1):
    _ALPHANUMERIC_CHARACTER_TABLE[chr(i)] = (i - ord("A")) + 10

# bits use in character count indicator
_NUMERIC_CHARACTER_COUNT_BITS = [10, 12, 14]
_ALPHANUMERIC_CHARACTER_COUNT_BITS = [9, 11, 13]
_BYTE_CHARCTER_COUNT_BITS = [8, 16, 16]

def _get_char_count_bits(mode: 'types.Mode', version: int) -> int:
    """
    Get number of bits used to specify character count based on 
    mode and version
    """
    lookup_index = -1

    if 1 <= version and version <= 9:
        lookup_index = 0
    elif 10 <= version and version <= 26:
        lookup_index = 1
    elif 27 <= version and version <= 40:
        lookup_index = 2

    match mode:
        case types.Mode.NUMERIC:
            return _NUMERIC_CHARACTER_COUNT_BITS[lookup_index]
        case types.Mode.ALPHANUMERIC:
            return _ALPHANUMERIC_CHARACTER_COUNT_BITS[lookup_index]
        case types.Mode.BYTE:
            return _BYTE_CHARCTER_COUNT_BITS[lookup_index]
        case _:
            # this branch should be unreachable if correct types are passed into this function
            raise TypeError("Invalid mode specifier")
