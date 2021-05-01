special_characters1 = '"!#$%&*()-+,/"|" "./\''
special_characters2 = ':;<>=?@'
special_characters3 = '[]\\^_`'
special_characters4 = '{}|~'
numeric_characters = '0123456789'


class CipherCeasarSalad:

    def cipher(text, shiftBy):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char in special_characters1:
                result += chr((ord(char) + shiftBy - 32) % 16 + 32)
            elif char in special_characters2:
                result += chr((ord(char) + shiftBy - 58) % 7 + 58)
            elif char in special_characters3:
                result += chr((ord(char) + shiftBy - 91) % 6 + 91)
            elif char in special_characters4:
                result += chr((ord(char) + shiftBy - 123) % 4 + 123)
            elif char in numeric_characters:
                result += chr((ord(char) + shiftBy - 48) % 10 + 48)
            elif char.isupper():
                result += chr((ord(char) + shiftBy - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shiftBy - 97) % 26 + 97)
        return result

    def decipher(text, shiftBy):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char in special_characters1:
                result += chr((ord(char) - shiftBy - 32) % 16 + 32)
            elif char in special_characters2:
                result += chr((ord(char) - shiftBy - 58) % 7 + 58)
            elif char in special_characters3:
                result += chr((ord(char) - shiftBy - 91) % 6 + 91)
            elif char in special_characters4:
                result += chr((ord(char) - shiftBy - 123) % 4 + 123)
            elif char in numeric_characters:
                result += chr((ord(char) - shiftBy - 48) % 10 + 48)
            elif char.isupper():
                result += chr((ord(char) - shiftBy - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shiftBy - 97) % 26 + 97)
        return result


if __name__ == '__main__':
    text = input("please enter text to entrypt...")
    shift = int(input("shift by.."))
    ciperText = CipherCeasarSalad.cipher(text, shift)
    print("Ciper Text %s: " % ciperText)
    deciperTest = CipherCeasarSalad.decipher(ciperText, shift)
    print("DeCiper Text %s: " % deciperTest)
