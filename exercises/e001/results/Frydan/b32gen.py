#!/bin/python3

import argparse
import random

parser = argparse.ArgumentParser(description='Base32 (RFC 4648) random character string generator')
meg = parser.add_mutually_exclusive_group()
parser.add_argument('characters', type=int, default=32, nargs='?', help='Number of characters to generate (default: 32)')
meg.add_argument('-l', '--lowercase', action='store_false', help='Output all lowercase (default choice)')
meg.add_argument('-u', '--uppercase', action='store_true', help='Output all uppercase')

args = parser.parse_args()

# main function for generating base32 strings
def getString(numOfCharacters, notLowercase):
	buff = ''
	for _ in range(numOfCharacters):
		rnd = random.randrange(0, 32)
		# A (0) - Z (25) Characters
		if rnd < 26:
			buff += chr(rnd+65)
		# 2 (26) - 7 (31) Characters, 
		# 0 and 1 are skipped for RFC 4648
		else:
			buff += chr(rnd+24)
	if (notLowercase):
		return buff
	return buff.lower()


if __name__ == '__main__':
	print(getString(args.characters, args.lowercase))
