import argparse
import random

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument("size", help="sets length of chain", nargs='?', const=32, type=int, default=32)
group.add_argument("-l", "--lowercase",  help="set letters to lowercase",  action='store_true', dest="case")
group.add_argument("-u", "--uppercase", help = "set letters to uppercase", action='store_false', dest='case')
args = parser.parse_args()

base32 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'

def genString(size, toLower=False):
	output = ''.join(random.choice(base32) for _ in range(size))
	if toLower == True:
		return output.lower()
	else:
		return output
	
print(genString(args.size, args.case))


