# Python program to for Morse Code encrypter and decrypter
# under category of cryptography

##################
# VARIABLES USED #
##################
# 'morseCodeDict' -> contains all the key and value
# 's1' -> takes user input in english
# 's2' -> keeps the encrypted message
# 's3' -> takes user input in morse code format
# 's4' -> temp var. for each morse char.
# 's5' -> keeps the decrypted message
# 'choice' -> ask user for encrypt or decrypt
# 'morseCodeDictTuple' -> the dict. func. keeps key + value in tuple.
# 'morseCodeDictList' -> convert the tuple in list data type

# Dictionary representing the morse code chart
# the chart is here: https://goo.gl/hPR4jA
morseCodeDict = {'A': '.-', 'B': '-...',
                 'C': '-.-.', 'D': '-..', 'E': '.',
                 'F': '..-.', 'G': '--.', 'H': '....',
                 'I': '..', 'J': '.---', 'K': '-.-',
                 'L': '.-..', 'M': '--', 'N': '-.',
                 'O': '---', 'P': '.--.', 'Q': '--.-',
                 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',
                 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                 '1': '.----', '2': '..---', '3': '...--',
                 '4': '....-', '5': '.....', '6': '-....',
                 '7': '--...', '8': '---..', '9': '----.',
                 '0': '-----'}

# Convert the dictionary element to list
# this is used for decrypting
morseCodeDictTuple = morseCodeDict.items()  # Dict. func. to get key and value
morseCodeDictList = []
for element in morseCodeDictTuple:
    morseCodeDictList += element
lim1 = len(morseCodeDictList)

# Welcome screen!
print(r"""
  _    _      _ _          _____                  _                              _               
 | |  | |    | | |        / ____|                | |                            | |              
 | |__| | ___| | | ___   | |     _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__   ___ _ __ 
 |  __  |/ _ \ | |/ _ \  | |    | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \ / _ \ '__|
 | |  | |  __/ | | (_) | | |____| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | |  __/ |   
 |_|  |_|\___|_|_|\___/   \_____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\___|_|   
                                       __/ | |              __/ |         | |                    
                                      |___/|_|             |___/          |_|                    
""")  # reason for r""" > https://github.com/PyCQA/pylint/issues/264

# Internal choice: encrypt or dcrypt
choice = int(input("Press 1 for encrypt or 2 for dcrypt:"))
if choice == 1:
    # Function to encrypt the string
    s1 = input("Enter a string:").upper()  # convert the string to CAPITAL
    s2 = ""
    for letter in s1:
        if letter != ' ':
            s2 += morseCodeDict[letter]+" "
        elif letter == " ":
            s2 += "  "
        else:
            print("Error")
    print(s2)
elif choice == 2:
    # Function to decrypt the MorseCode
    s3 = input("Enter Morse code string (add extra space in end):")
    s4 = ""
    s5 = ""
    for dot in s3:
        if dot != " ":
            s4 += dot
        elif dot == " ":
            for b in range(lim1):
                if morseCodeDictList[b] == s4:
                    # match value -> go back a step for key
                    s5 += morseCodeDictList[b-1]
                    break  # break is used to stop looping after getting the value
            if s4 == "":  # when it's a space s4 will be empty
                s5 += " "  # so add a space in final output var
            s4 = ""  # set empty s4 for next char.
        else:
            print("Error")
    print(s5)
# End the code for wrong input
else:
    print("** Invalid Input **")
