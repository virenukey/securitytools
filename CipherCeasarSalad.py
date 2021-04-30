class CipherCeasarSalad:
    def cipher(text, shiftBy):
        result = ""
        special_characters = '"!@#$%^&*()-+?_=,<>/"[]|\\{}" "./:;~`|\''
        for i in range(len(text)):
            char = text[i]
            if char in special_characters:
                result += str(ord(char))
            elif char.isnumeric():
                result += str(ord(char))
            elif isinstance(char, int):
                result += str(ord(char))
            elif char.isupper():
                result += chr((ord(char) + shiftBy-65) % 26 + 65)
            else:
                result += chr((ord(char) + shiftBy - 97) % 26 + 97)
        return result


if __name__ == '__main__':
    text = input("please enter text to entrypt...")
    shift = int(input("shift by.."))
    ciperText = CipherCeasarSalad.cipher(text, shift)
    print(ciperText)
