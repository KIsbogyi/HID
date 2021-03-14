import time
keyset = {
"a": "0x04", # Keyboard a and A
"b": "0x05", # Keyboard b and B
"c": "0x06",# Keyboard c and C
"d": "0x07", # Keyboard d and D
"e": "0x08", # Keyboard e and E
"f": "0x09", # Keyboard f and F
"g": "0x0a", # Keyboard g and G
"h": "0x0b", # Keyboard h and H
"i": "0x0c", # Keyboard i and I
"j": "0x0d", # Keyboard j and J
"k": "0x0e", # Keyboard k and K
"l": "0x0f", # Keyboard l and L
"m": "0x10", # Keyboard m and M
"n": "0x11", # Keyboard n and N
"o": "0x12", # Keyboard o and O
"p": "0x13", # Keyboard p and P
"q": "0x14", # Keyboard q and Q
"r": "0x15", # Keyboard r and R
"s": "0x16", # Keyboard s and S
"t": "0x17", # Keyboard t and T
"u": "0x18", # Keyboard u and U
"v": "0x19", # Keyboard v and V
"w": "0x1a", # Keyboard w and W
"x": "0x1b", # Keyboard x and X
"z": "0x1c", # Keyboard y and Y
"y": "0x1d", # Keyboard z and Z
"enter": "0x28",
"space": "0x2C",
"backslash": "0x31",
}
numbers = ["0","1","2","3","4","5","6","7","8","9"]
fbe = open("1.txt","r")

helper = True
number = ""

for data in fbe:
    for x in data:
        if x == "\\" and helper == True:
            helper = False
        elif x != "\\" and helper == False:
            print(keyset["backslash"])
            helper = True
        elif x == "\\" and helper == False:
            helper = True
        elif x in numbers:
            helper = True
            number += str(x)
        elif number != "":
            time.sleep(int(number))
            number = ""
        else:
            print(x)
