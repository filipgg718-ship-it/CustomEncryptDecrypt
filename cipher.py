
# Custom Symbol Encryption / Decryption System
# Python 3.x

import os

# Your custom alphabet
CIPHER = {
    "Q": r"""]@]{,""",
    "W": r"""!\\//!""",
    "E": r"""<\\>":\|""",
    "R": r"""o_+<\{]""",
    "T": r"""i1'//.;{}""",
    "Y": r"""|_+||""",
    "U": r"""O)(()""",
    "I": r"""!{]1!""",
    "O": r"""5-{""",
    "P": r"""i++-O""",
    "A": r"""\\>\|||\\ """.rstrip(),
    "S": r"""())(()""",
    "D": r"""I||\0""",
    "F": r"""|_+-||14""",
    "G": r"""{}:L""",
    "H": r"""\,\|.|\.,\.""",
    "J": r""":})0""",
    "K": r"""\]\]/""",
    "L": r"""'{']|""",
    "Z": r"""e{./"]""",
    "X": r"""|?\/y0{""",
    "C": r"""Ioo(=+}{":""",
    "V": r""";;'/.[{]\ """.rstrip(),
    "B": r'''"{]''/>''',
    "N": r""";'}{"?""",
    "M": r""";'.<_+_)./""",
}

# Build reverse lookup for decryption
REVERSE_CIPHER = {value: key for key, value in CIPHER.items()}

# Separator makes each encrypted letter unambiguous
SEPARATOR = "~"
SPACE_TOKEN = "<SPACE>"


def encrypt(message):
    tokens = []

    for char in message:
        upper_char = char.upper()

        if char == " ":
            tokens.append(SPACE_TOKEN)
        elif upper_char in CIPHER:
            tokens.append(CIPHER[upper_char])
        else:
            # Keep punctuation, digits and unknown characters
            tokens.append(char)

    return SEPARATOR.join(tokens)


def decrypt(encrypted_message):
    tokens = encrypted_message.split(SEPARATOR)
    result = []

    for token in tokens:
        if token == SPACE_TOKEN:
            result.append(" ")
        elif token in REVERSE_CIPHER:
            result.append(REVERSE_CIPHER[token])
        else:
            result.append(token)

    return "".join(result)


def show_alphabet():
    print("\nYour custom alphabet:\n")
    for letter, symbol in CIPHER.items():
        print(f"{letter} = {symbol}")


def main():
    while True:
        print("\n===== CUSTOM CIPHER =====")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Show alphabet")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            message = input("Enter your message: ")
            print("\nEncrypted message:")
            print(encrypt(message))

        elif choice == "2":
            message = input("Enter encrypted message: ")
            print("\nDecrypted message:")
            print(decrypt(message))

        elif choice == "3":
            show_alphabet()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Choose 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
