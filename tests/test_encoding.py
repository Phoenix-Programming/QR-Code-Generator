from bitarray import bitarray

from qr_generator.encoding import _encode_numeric, _encode_alphanumeric, _encode_byte

def test_encoding_numeric():

    # test case taken from ISO 18004: 2024
    data = "01234567"

    expected = bitarray("0001 0000001000 0000001100 0101011001 1000011")
    actual = _encode_numeric(data, version=1)

    assert expected == actual


def test_encoding_alphanumeric():
    data = "HELLO WORLD"

    expected = bitarray("0010 000001011 01100001011 01111000110 10001011100 10110111000 10011010100 001101")
    actual = _encode_alphanumeric(data, version=1)

    assert expected == actual


def test_encoding_bytes():
    data = "Hèllo, wörld!"

    expected = bitarray("0100 00001101 01001000 11101000 01101100 01101100 01101111 00101100 00100000 01110111 11110110 01110010 01101100 01100100 00100001")
    actual = _encode_byte(data, version=1)

    assert expected == actual

