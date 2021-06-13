import random
import base64
import argparse

parser = argparse.ArgumentParser(description="Random string of base32 characters")
parser.add_argument('characters', default=32, type=int, nargs='?', help='How many characters to print, default=32')
caseGroup = parser.add_mutually_exclusive_group()
caseGroup.add_argument('-l', '--lower', action='store_true', dest='size', help='Printing all lower characters')
caseGroup.add_argument('-u', '--upper', action='store_false', dest='size', help='Printing all upper characters')

args = parser.parse_args()


def random_string(n):
    a = [random.randint(0, 255) for _ in range(n)]
    b = bytes(a)
    z = base64.b32encode(b)
    if args.size:
        return z.lower()
    else:
        return z.upper()


if __name__ == '__main__':
    n = args.characters
    s = random_string(n)[:n]
    print(s.decode('ascii'))
