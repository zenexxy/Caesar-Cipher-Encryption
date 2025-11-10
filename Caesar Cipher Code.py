print("Hey There! This program will encrypt and decrypt your chosen phrases or words.")
print()
phrase = input("Please enter a phrase/word to be encrypted and decrypted: ")
#Constants for the Code
ASCII_VALUE_OF_a = 97
ASCII_VALUE_OF_z = 122
ASCII_VALUE_OF_space = 32
ASCII_VALUE_OF_A = 65
ASCII_VALUE_OF_Z = 90
ASCII_VALUE_OF_asterisk = 42
TOTAL_LETTERS_IN_THE_ALPHABET = 26

# Function to encrypt the given text
def encrypt(text):
    result = ""  # an empty string to store the encrypted result

    for i in text: #Use a for loop to individually check each character for their ascii value

        ascii = ord(i)  # Get the ASCII value of the characters

        if ascii >= ASCII_VALUE_OF_a and ascii <= ASCII_VALUE_OF_z:  # Check if the character is lowercase
            ascii -= 32 # Shift ASCII value to be Uppercase
            ascii += 3  # Shift ASCII value by 3

            if ascii > ASCII_VALUE_OF_Z and ascii < ASCII_VALUE_OF_a: # Check if the ASCII value is over Z and less than a
                ascii -= TOTAL_LETTERS_IN_THE_ALPHABET
            
            result +=chr(ascii)

        elif ascii >= ASCII_VALUE_OF_A and ascii <= ASCII_VALUE_OF_Z:  # Check if the character is uppercase
            ascii += 32 # Shift ASCII value by 32 to be Lowercase
            ascii -= 3  # Shift ASCII value by -3

            if ascii < ASCII_VALUE_OF_a and ascii > ASCII_VALUE_OF_Z: # Check if the ASCII value is over Z and less than a
                ascii += TOTAL_LETTERS_IN_THE_ALPHABET
            
            result +=chr(ascii)

        else:  # this handles the spaces
            if ascii == ASCII_VALUE_OF_space:  # If the character is a space
                ascii = ASCII_VALUE_OF_asterisk  # Convert it to an asterisk '*'
                result += chr(ascii)

    return result

# Function to decrypt the given text
def decrypt(text):
    result = ""  # an empty string to store the decrypted results

    for i in text:  #Use a for loop to individually check each character for their ascii value
        ascii = ord(i)  # Get the ASCII value of the characters

        if ascii >= ASCII_VALUE_OF_a and ascii <= ASCII_VALUE_OF_z:  # Check if the character is lowercase
            ascii-= 32  # Change to uppercase
            ascii += 3  # Shift ASCII value by 3

            if ascii > ASCII_VALUE_OF_Z and ascii < ASCII_VALUE_OF_a: # Check if the ASCII value is over Z and less than a
                ascii -= TOTAL_LETTERS_IN_THE_ALPHABET
            
            result += chr(ascii)


        elif ascii >= ASCII_VALUE_OF_A and ascii <= ASCII_VALUE_OF_Z:  # Check if the character is uppercase
            ascii += 32 # Change to lowercase
            ascii -= 3  # Shift ASCII value by -3

            if ascii < ASCII_VALUE_OF_a and ascii > ASCII_VALUE_OF_Z: # Check if the ASCII value is over Z and less that a
                ascii += TOTAL_LETTERS_IN_THE_ALPHABET
            
            result += chr(ascii)


        else:  # Handle non-alphabetic characters
            if ascii == ASCII_VALUE_OF_asterisk:  # If the character is an asterisk '*'
                ascii = ASCII_VALUE_OF_space  # Convert it back to a space
                result += chr(ascii)
    return result

# Encrypt the user's phrase and store it
encrpytedPhrase = encrypt(phrase)

print("")
# Display the encrypted phrase
print("The encrypted version of the phrase/word is", encrypt(phrase))

print("")
# Display the decrypted phrase
print("The decrypted version of the phrase/word is", decrypt(encrpytedPhrase))
