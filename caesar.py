#!/usr/bin/env python3
import argparse

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            rotated = chr((ord(char) - base + shift) % 26 + base)
            result += rotated
        else:
            result += char
    return result

def bruteforce(text):
    results = []
    for s in range(26):
        results.append((s, caesar_cipher(text, -s)))
    return results

def main():
    try:
        parser = argparse.ArgumentParser(
            description="Caesar Cipher Tool — Encrypt, Decrypt, Bruteforce"
        )

        parser.add_argument(
            "-e", "--encrypt",
            help="Encrypt a message",
            action="store_true"
        )

        parser.add_argument(
            "-d", "--decrypt",
            help="Decrypt a message with a shift",
            action="store_true"
        )

        parser.add_argument(
            "-b", "--bruteforce",
            help="Try all possible shifts (0–25)",
            action="store_true"
        )

        parser.add_argument(
            "-s", "--shift",
            help="Rotation shift (0–25)",
            type=int
        )

        parser.add_argument(
            "-t", "--text",
            help="Text to process",
            type=str
        )

        args = parser.parse_args()

        if not args.text:
            print("❌ ERROR: You must provide text using -t")
            return

        if args.encrypt:
            if args.shift is None:
                print("❌ ERROR: Encryption requires -s shift value.")
                return
            print(caesar_cipher(args.text, args.shift))

        elif args.decrypt:
            if args.shift is None:
                print("❌ ERROR: Decryption requires -s shift value.")
                return
            print(caesar_cipher(args.text, -args.shift))

        elif args.bruteforce:
            for s, result in bruteforce(args.text):
                print(f"Shift {s:2}: {result}")

        else:
            print("❌ ERROR: You must choose -e, -d, or -b")
    
    except Exception as e:
        print(f"🔥 ERROR: {e}")

if __name__ == "__main__":
    main()
