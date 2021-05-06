import argparse
import string
import random

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("size", help="sets length of chain", nargs='?', const=32, type=int, default=32)
group.add_argument("-l", "--lowercase",  help="set letters to lowercase",  action='store_true')
group.add_argument("-u", "--uppercase", help = "set letters to uppercase", action='store_true')
args = parser.parse_args()

def genString(size, toLower=False):
	if toLower==True:
		output = ''.join(random.choice(string.ascii_uppercase) for _ in range(size)).lower()
	else:
		output = ''.join(random.choice(string.ascii_uppercase) for _ in range(size))
	print(output)

genString(args.size, args.lowercase)


