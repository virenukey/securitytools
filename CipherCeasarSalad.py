import sys

special_characters1 = '"!#$%&*()-+,/"|" "./\''
special_characters2 = ':;<>=?@'
special_characters3 = '[]\\^_`'
special_characters4 = '{}|~'
numeric_characters = '0123456789'


class CipherCeasarSalad:

    def cipher(text, shiftBy):
        text1 = text.split("\n")
        final_result = []
        for text in text1:
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
            final_result.append(result)
        final_ciper_text = "\n".join(final_result)
        return final_ciper_text

    def decipher(text, shiftBy):
        text1 = text.split("\n")
        final_result = []
        for text in text1:
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
            final_result.append(result)
        final_deciper_text = "\n".join(final_result)
        return final_deciper_text


if __name__ == '__main__':
    print("Enter/Paste your text (can be multiline)..")
    text = []
    while True:
        line = input()
        if not line:
            break
        else:
            text.append(line)
    text = '\n'.join(text)
    shift = int(input("shift by.."))
    multilineCiperText = CipherCeasarSalad.cipher(text, shift)
    cip = multilineCiperText.split("\n")
    ciperText = "%$#".join(cip)
    print("Ciper Text: %s" % ciperText)
    deciperTest = CipherCeasarSalad.decipher(multilineCiperText, shift)
    print("DeCiper Text: %s" % deciperTest)
