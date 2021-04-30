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

def generateString(keySize =arg.size, charCase = arg.u, ):
    keyGenerated = ""          

    
    for _ in range(keySize):

        keyGenerated += (random.choice(string.ascii_uppercase + string.digits))
    if not charCase:
        keyGenerated = keyGenerated.lower()
    #print(keyGenerated, len(keyGenerated))
    print (keyGenerated)

     

generateString()



