import time
import random

while True:
    characters = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ",", ".", ";", ":", "<", ">", "*", "+", "[", "]", "{", "}", "ç", "¿", "?", "¡", "!", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "|", "º", "ª", "/", "&", "%", "$", "·", "#", "@", "=", "¬")
    charactNum = int(input("Select the number of characters (write 0 for random character's numer): "))
    passwordList = []

    if charactNum == 0:
        randomNum = random.randint(10, 100)
        for i in range(randomNum):
            passwordList.append(characters[random.randint(0, len(characters) - 1)])
    else:
        for i in range(charactNum):
            passwordList.append(characters[random.randint(0, len(characters) - 1)])

    password = "".join(passwordList)
    print (password, "\n")
    
    time.sleep(10)