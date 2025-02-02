from exceptions import (LengthBinaryError,
                        DigitBinaryError,
                        ZeroOneError)


class BinaryConverter:
    def __init__(self, binary: str):
        if len(binary) > 8:
            raise LengthBinaryError()
        elif not binary.isdigit():
            raise DigitBinaryError()
        elif binary.find('0') == -1 or binary.find('1') == -1:
            raise ZeroOneError()
        else:
            self._binary: str = binary

    def to_decimal(self):
        return int(self._binary, 2)