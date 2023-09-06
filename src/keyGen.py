import os
import argparse
import secrets
import sys  # Import the 'sys' module for system-specific parameters and functions
import utilities
# Add the '../data' directory to the Python path, allowing you to import modules from there
os.sys.path.append('../data')
# Import specific functions from the 'utilities' module
from utilities import writekeys

def parseArgs(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lamda', type=int,help='Enter the Value of Lamda')
    opts = parser.parse_args()
    return opts

def generate_secret_key(bits):
    if bits % 8 != 0:
        raise ValueError("Number of bits must be a multiple of 8")
    
    num_bytes = bits // 8
    key = secrets.token_hex(num_bytes)
    return key


def KeyGen(opts):
    lambda_bits = opts.lamda
    if 1 <= lambda_bits <= 128:
        # Generate a random secret key as a hexadecimal string
        key=generate_secret_key(lambda_bits)
        print(key)
        writekeys(key)


if __name__ == "__main__":
    opts = parseArgs(sys.argv)
    KeyGen(opts)


## Code Devloped by Mabon Ninan
## Under the Suprivion of Dr. Boyang
### UCDASec