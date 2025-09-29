from enum import IntEnum, Enum

class Mode(IntEnum):
    """Represents which mode the QR code uses"""
    NUMERIC = 0b0001
    ALPHANUMERIC  = 0b0010
    BYTE = 0b0100

    __str__ = Enum.__str__

class ErrorCorrection(IntEnum):
    """Represents error correction level of the QR code"""
    L = 0b01
    M = 0b00
    Q = 0b11
    H = 0b10

    __str__ = Enum.__str__

