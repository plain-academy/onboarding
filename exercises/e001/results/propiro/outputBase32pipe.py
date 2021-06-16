#!/usr/bin/env python3

import os
import sys
import string
import random
import argparse

parser = argparse.ArgumentParser(description='base32 key generator script')
parser.add_argument('size', const=32, default=32, type=int, help='size of key, default=32', nargs='?')
caseGroup = parser.add_mutually_exclusive_group()
caseGroup.add_argument('-u', action="store_true", help='use uppercase letters, default option', default=True)
caseGroup.add_argument('-l', action="store_true", help='use lowercase letters', default=False)

arg = parser.parse_args()

arg.u = not arg.l

def generateString(keySize, charCase):
    keyGenerated = ""          
    base32chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
    
    for _ in range(keySize):
        keyGenerated += (random.choice(base32chars))
    if not charCase:
        keyGenerated = keyGenerated.lower()
    #print(keyGenerated, len(keyGenerated))
    print (keyGenerated)

#generateString(arg.size, arg.u)


def main():
    try:
        generateString(arg.size, arg.u)
        sys.stdout.flush()
    except (BrokenPipeError):
        print ("_")
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        sys.exit(1)

if __name__ == '__main__':
    main()
