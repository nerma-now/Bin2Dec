---
name: Bin2Dec
about: Binary-to-Decimal number converter
---

## Summary
Binary is the number system all digital computers are based on. Therefore it's important for developers to understand binary, or base 2, mathematics. The purpose of Bin2Dec is to provide practice and understanding of how binary calculations.

Bin2Dec allows the user to enter strings of up to 8 binary digits, 0's and 1's, in any sequence and then displays its decimal equivalent.

### Basic example
The same code can be examined in the `main.py` file.

```python
from converter import BinaryConverter

def main() -> None:
    binary: str = input('Enter binary digits (Maximum 8 characters): ')

    binary_converter:BinaryConverter = BinaryConverter(binary)
    decimal: int = binary_converter.to_decimal()

    print(decimal)

if __name__ == '__main__':
    main()
```

### Motivation
The desire to develop and learn new things. I took the idea for this project from an open repository from **Florin Pop** [(florinpop17)](https://github.com/florinpop17/app-ideas/blob/master/Projects/1-Beginner/Bin2Dec-App.md)