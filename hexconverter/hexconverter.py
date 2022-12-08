alphabet = ['20', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71',
            '72', '73', '74', '75', '76', '77', '78', '79', '7a', '41', '42', '43', '44', '45', '46', '47', '48', '49',
            '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a']

symbols = "21 40 23 24 25 5e 26 2a 28 29 2d 3d 5f 2b 7b 5b 7d 5d 7c 5c 3a 3b 22 27 3c 2c 3e 2e 7e 60".split()

numbers = "30 31 32 33 34 35 36 37 38 39".split()


class hex_to_string:
    output = str()


def hex_to_string(string):
    y = ""
    for char in string:

        if char == " ":
            y = y + alphabet[0]
        elif char == "a":
            y = y + alphabet[1]
        elif char == "b":
            y = y + alphabet[2]
        elif char == "c":
            y = y + alphabet[3]
        elif char == "d":
            y = y + alphabet[4]
        elif char == "e":
            y = y + alphabet[5]
        elif char == "f":
            y = y + alphabet[6]
        elif char == "g":
            y = y + alphabet[7]
        elif char == "h":
            y = y + alphabet[8]
        elif char == "i":
            y = y + alphabet[9]
        elif char == "j":
            y = y + alphabet[10]
        elif char == "k":
            y = y + alphabet[11]
        elif char == "l":
            y = y + alphabet[12]
        elif char == "m":
            y = y + alphabet[13]
        elif char == "n":
            y = y + alphabet[14]
        elif char == "o":
            y = y + alphabet[15]
        elif char == "p":
            y = y + alphabet[16]
        elif char == "q":
            y = y + alphabet[17]
        elif char == "r":
            y = y + alphabet[18]
        elif char == "s":
            y = y + alphabet[19]
        elif char == "t":
            y = y + alphabet[20]
        elif char == "u":
            y = y + alphabet[21]
        elif char == "v":
            y = y + alphabet[22]
        elif char == "w":
            y = y + alphabet[23]
        elif char == "x":
            y = y + alphabet[24]
        elif char == "y":
            y = y + alphabet[25]
        elif char == "z":
            y = y + alphabet[26]
        elif char == "A":
            y = y + alphabet[27]
        elif char == "B":
            y = y + alphabet[28]
        elif char == "C":
            y = y + alphabet[29]
        elif char == "D":
            y = y + alphabet[30]
        elif char == "E":
            y = y + alphabet[31]
        elif char == "F":
            y = y + alphabet[32]
        elif char == "G":
            y = y + alphabet[33]
        elif char == "H":
            y = y + alphabet[34]
        elif char == "I":
            y = y + alphabet[35]
        elif char == "J":
            y = y + alphabet[36]
        elif char == "K":
            y = y + alphabet[37]
        elif char == "L":
            y = y + alphabet[38]
        elif char == "M":
            y = y + alphabet[39]
        elif char == "N":
            y = y + alphabet[40]
        elif char == "O":
            y = y + alphabet[41]
        elif char == "P":
            y = y + alphabet[42]
        elif char == "Q":
            y = y + alphabet[43]
        elif char == "R":
            y = y + alphabet[44]
        elif char == "S":
            y = y + alphabet[45]
        elif char == "T":
            y = y + alphabet[46]
        elif char == "U":
            y = y + alphabet[47]
        elif char == "V":
            y = y + alphabet[48]
        elif char == "W":
            y = y + alphabet[49]
        elif char == "X":
            y = y + alphabet[50]
        elif char == "Y":
            y = y + alphabet[51]
        elif char == "Z":
            y = y + alphabet[52]

        if char == "!":
            y = y + symbols[0]
        elif char == "@":
            y = y + symbols[1]
        elif char == "#":
            y = y + symbols[2]
        elif char == "$":
            y = y + symbols[3]
        elif char == "%":
            y = y + symbols[4]
        elif char == "^":
            y = y + symbols[5]
        elif char == "&":
            y = y + symbols[6]
        elif char == "*":
            y = y + symbols[7]
        elif char == "(":
            y = y + symbols[8]
        elif char == ")":
            y = y + symbols[9]
        elif char == "-":
            y = y + symbols[10]
        elif char == "=":
            y = y + symbols[11]
        elif char == "_":
            y = y + symbols[12]
        elif char == "+":
            y = y + symbols[13]
        elif char == "{":
            y = y + symbols[14]
        elif char == "[":
            y = y + symbols[15]
        elif char == "}":
            y = y + symbols[16]
        elif char == "]":
            y = y + symbols[17]
        elif char == "|":
            y = y + symbols[18]
        elif char == "\\":
            y = y + symbols[19]
        elif char == ":":
            y = y + symbols[20]
        elif char == ";":
            y = y + symbols[21]
        elif char == '"':
            y = y + symbols[22]
        elif char == "'":
            y = y + symbols[23]
        elif char == "<":
            y = y + symbols[24]
        elif char == ",":
            y = y + symbols[25]
        elif char == ">":
            y = y + symbols[26]
        elif char == ".":
            y = y + symbols[27]
        elif char == "/":
            y = y + symbols[28]
        elif char == "?":
            y = y + symbols[29]
        elif char == "~":
            y = y + symbols[30]
        elif char == "`":
            y = y + symbols[31]

        if char == "0":
            y = y + numbers[0]
        if char == "1":
            y = y + numbers[1]
        if char == "2":
            y = y + numbers[2]
        if char == "3":
            y = y + numbers[3]
        if char == "4":
            y = y + numbers[4]
        if char == "5":
            y = y + numbers[5]
        if char == "6":
            y = y + numbers[6]
        if char == "7":
            y = y + numbers[7]
        if char == "8":
            y = y + numbers[8]
        if char == "9":
            y = y + numbers[9]
        y = y + " "

    hex_to_string.output = y


__version__ = 'dev'
