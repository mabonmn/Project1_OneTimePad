# Import necessary libraries and modules
import numpy as np  # Import NumPy library and alias it as 'np'
import os  # Import the 'os' module for file and directory operations
import sys  # Import the 'sys' module for system-specific parameters and functions
import utilities  
# Add the '../data' directory to the Python path, allowing you to import modules from there
os.sys.path.append('../data')

# Import specific functions from the 'utilities' module
from utilities import loadKey, loadPlaintext, loadCiphertxt, writeCiphertxt, binary_xor, otp_encrypt, text_to_binary

# Define the main encryption function
def Enc():
    # Load the secret key from a file
    sk = loadKey()
    
    # Load the plaintext from a file
    m = loadPlaintext()
    
    # Initialize an empty list to store the ciphertext
    ciphertext = []
    
    print("CIPHERTEXT")
    
    # Loop through each element in the plaintext
    for i in range(len(m)):
        # Convert the plaintext to binary representation
        binary_text = text_to_binary(m[i])
        
        # Check if the binary text has the same length as the secret key
        if len(binary_text) != len(sk):
            print("error: length is incorrect!")
            continue
        else:
            # Encrypt the binary plaintext using OTP (One-Time Pad)
            temp = otp_encrypt(binary_text, sk)
            print(temp)
            
            # Append the encrypted text to the ciphertext list
            ciphertext.append(temp)
    
    # Write the ciphertext to a file
    writeCiphertxt(ciphertext)

# Entry point of the script
if __name__ == "__main__":
    Enc()  # Call the encryption function when the script is executed



## Code Devloped by Mabon Ninan
## Under the Suprivion of Dr. Boyang
### UCDASec
