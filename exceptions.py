class LengthBinaryError(Exception):
    def __init__(self):
        super().__init__('The length of binary digits in one input field should not exceed 8 characters')

class DigitBinaryError(Exception):
    def __init__(self):
        super().__init__('A string of binary digits cannot contain any other characters')

class ZeroOneError(Exception):
    def __init__(self):
        super().__init__('The characters you enter can only be zeros (0) or ones (1)')