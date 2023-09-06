# Function to load the secret key from a file
def loadKey():
    # Define the path to the key file
    file_path = 'data/key.txt'

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the entire contents of the file into a string
        file_contents = file.read()
    
    # Return the contents of the key file
    return file_contents

# Function to load plaintext from a file
def loadPlaintext():
    # Define the path to the plaintext file
    file_path = 'data/plaintext.txt'

    # Initialize an empty list to store the words
    word_array = []

    # Open the plaintext file for reading
    with open(file_path, 'r') as file:
        # Read the content of the file and split it into words
        words = file.read().split()

        # Add each word to the word_array
        word_array.extend(words)
    
    # Return the list of words from the plaintext file
    return word_array

# Function to load ciphertext from a file
def loadCiphertxt():
    # Define the path to the ciphertext file
    file_path = 'data/ciphertext.txt'

    try:
        # Try to open the ciphertext file for reading
        with open(file_path, "r") as file:
            # Read each line of the file into an array
            array = [line.strip() for line in file]
        return array
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"File '{file_path}' not found.")
        return []

# Function to write ciphertext to a file
def writeCiphertxt(ciphertext):
    # Define the path to the output ciphertext file
    output_file_path = 'data/ciphertext.txt'
    with open(output_file_path, "w") as file:
        # Write each item in the ciphertext array to the file, one per line
        for item in ciphertext:
            file.write(str(item) + "\n")

# Function to write results to a file
def writeResults(plaintext):
    # Define the path to the output result file
    output_file_path = 'data/result.txt'
    with open(output_file_path, "w") as file:
        # Write each item in the plaintext array to the file, one per line
        for item in plaintext:
            file.write(str(item) + "\n")

# Function to perform a binary XOR operation on two binary strings
def binary_xor(str1, str2):
    return ''.join('1' if bit1 != bit2 else '0' for bit1, bit2 in zip(str1, str2))

# Function to perform OTP (One-Time Pad) encryption
def otp_encrypt(plaintext, secret_key):
    # Perform binary XOR between the plaintext and the secret key
    ciphertext = binary_xor(plaintext, secret_key)
    return ciphertext

# Function to convert text to binary representation
def text_to_binary(text):
    # Convert each character in the text to an 8-bit binary representation
    binary_result = ''.join(format(ord(char), '08b') for char in text)
    return binary_result

# Function to convert binary representation back to text
def binary_to_text(binary_str):
    text = ""
    # Convert binary back to characters, assuming 8-bit characters
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        text += chr(int(byte, 2))
    return text

def writekeys(keys):
    # Define the path to the output ciphertext file
    output_file_path = 'data/newkey.txt'
    with open(output_file_path, "w") as file:
        # Write each item in the ciphertext array to the file, one per line
        file.write(str(keys) + "\n")

## Code Devloped by Mabon Ninan
## Under the Suprivion of Dr. Boyang
### UCDASec