from converter import BinaryConverter

def main() -> None:
    binary: str = input('Enter binary digits (Maximum 8 characters): ')

    binary_converter:BinaryConverter = BinaryConverter(binary)
    decimal: int = binary_converter.to_decimal()

    print(decimal)

if __name__ == '__main__':
    main()