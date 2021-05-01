import random
import string
import base64
import argparse

parser = argparse.ArgumentParser(description="Random string of base32 characters")
parser.add_argument('-a', '--amount', type=int, help='How many characters to print')
parser.add_argument('-u', '--upper', action='store_true', help='Printing all upper characters')
parser.add_argument('-l', '--lower', action='store_true', help='Printing all lower characters')
args = parser.parse_args()


def random_string(n):
    letters = string.ascii_letters + string.digits
    zz = (''.join(random.choice(letters) for i in range(n)))
    encoded = zz.encode("utf-8")
    b32coded = base64.b32encode(encoded)
    if args.upper:
        return b32coded.upper()
    elif args.lower:
        return b32coded.lower()
    else:
        return b32coded.upper()


if __name__ == '__main__':
    if args.amount is None:
        r_string = '%.34s' % random_string(32)
        print(r_string[2:])
    else:
        # ra_string = '%.s' % random_string(args.amount)
        # print(ra_string[2:])
        print(random_string(args.amount)) # doesn't work, I don't know how to truncate this string by args.amount
