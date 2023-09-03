#!/usr/bin/env python3
import argparse

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def main():
    parser = argparse.ArgumentParser(description='Caesar Encryption')
    parser.add_argument('text', type=str, help='The text to be encrypted')
    parser.add_argument('shift', type=int, help='The shift value for encryption')

    args = parser.parse_args()
    encrypted_text = caesar_encrypt(args.text, args.shift)
    print(encrypted_text)

if __name__ == "__main__":
    main()
