# Import necessary libraries and modules
import numpy as np  # Import NumPy library and alias it as 'np'
import os  # Import the 'os' module for file and directory operations
import sys  # Import the 'sys' module for system-specific parameters and functions
import utilities

# Add the '../data' directory to the Python path, allowing you to import modules from there
os.sys.path.append('../data')

# Import specific functions from the 'utilities' module
from utilities import loadKey, loadCiphertxt, writeResults, binary_xor, binary_to_text

# Define the main decryption function
def Dec():
    # Load the secret key from a file
    sk = loadKey()
    
    # Load the ciphertext from a file
    ciphertext = loadCiphertxt()
    
    # Initialize an empty list to store the decrypted plaintext
    plaintext = []
    
    print("DECRYPTED TEXT")
    
    # Loop through each element in the ciphertext
    for i in range(len(ciphertext)):
        # Check if the length of the ciphertext is the same as the secret key
        if len(ciphertext[i]) != len(sk):
            print("error: length is incorrect!")
            continue
        else:
            # Decrypt the ciphertext using XOR with the secret key and convert back to text
            temp = binary_to_text(binary_xor(ciphertext[i], sk))
            print(temp)
            
            # Append the decrypted text to the plaintext list
            plaintext.append(temp)
    
    # Write the decrypted plaintext to a file
    writeResults(plaintext)

# Entry point of the script
if __name__ == "__main__":
    decryption()  # Call the decryption function when the script is executed


## Code Devloped by Mabon Ninan
## Under the Suprivion of Dr. Boyang
### UCDASec
