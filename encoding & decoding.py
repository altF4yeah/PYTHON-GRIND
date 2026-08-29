# encoding/decoding

import random

letters = "abcdefghijklmnopqrstuvwxyz"

def encode():
    print()
    string = input("Enter Your word that you want to encode: ")
    if len(string) <3:
        encode = string[::-1]

    else:
        x = ""
        y = ""

        for i in range(0,3):
            x += random.choice(letters)
            y += random.choice(letters)

            encode =x + string[1:] + string[:1] + y

    print("Encoded text is", encode)

def decode():
    print()
    string = input("Enter Your word that you want to encode: ")
    if len(string) < 3:
        decode = string[::-1]

    else:
        decode =string[-4] + string[3:-4]
    
    print("Decoded text is", decode)

def encode_sentence():
    print()
    sentence = input("Enter Your sentence that you want to encode: ")
    words = sentence.split()
    result = []

    for string in words:
        if len(string) < 3:
            encoded = string[::-1]

        else:
            x = ""
            y = ""

            for i in range(0, 3):
                x += random.choice(letters)
                y += random.choice(letters)

            encoded = x + string[1:] + string[:1] + y

        result.append(encoded)

    print("Encoded sentence is", " ".join(result))

def decode_senence():
    print()
    sentence = input("Enter Your sentence that you want to decode: ")
    words = sentence.split()
    result = []

    for string in words:
        if len(string) < 3:
            decoded = string[::-1]

        else:
            decoded = string[-4] + string[3:-4]

        result.append(decoded)

    print("Decoded text is", " ".join(result))

def main():

    while True:
        print()
        print("Choose: ")
        print("1. Encode text")
        print("2. Decode text")
        print("3. Encode sentence")
        print("4. Decode sentence")

        choice = int(input("1, 2, 3 or 4 (0 to stop) "))

        if choice == 1:
            encode()

        elif choice == 2:
            decode()

        elif choice == 3:
            encode_sentence()

        elif choice == 4:
            decode_senence()

        elif choice == 0:
            print("stopping the program...")
            break

main()