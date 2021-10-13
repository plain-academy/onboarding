# Importing random to generate
# random string sequence
import random

# Importing string library function
import string

def rand_pass(size):

    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice(
                        string.ascii_letters + string.digits)
                                                for n in range(size)])

    return generate_pass

# Driver Code 
password = rand_pass(7) #change length of generated string
print(password.upper()) #print all symbols in uppercase
