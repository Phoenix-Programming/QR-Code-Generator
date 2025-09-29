from bitarray import bitarray

from qr_generator.encoding import _encode_numeric

def test_encoding_numeric():

    # test case taken from ISO 18004: 2024
    data = "01234567"

    expected = bitarray("0001 0000001000 0000001100 0101011001 1000011")
    actual = _encode_numeric(data, version=1)

    assert expected == actual

