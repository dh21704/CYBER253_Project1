mapping = {  #for letters a - z
    "a": "♬", "b": "♭", "c": "♮", "d": "♯", "e": "°", "f": "ø",  
    "g": "؂", "h": "≠", "i": "≭", "j": "☧", "k": "☨", "l": "☩",  
    "m": "☫", "n": "☬", "o": "☭", "p": "☯", "q": "☽", "r": "☾",  
    "s": "✙", "t": "✛", "u": "✜", "v": "✝", "w": "✞", "x": "✟",  
    "y": "‡", "z": "♁", 
    #numbers start here
    "0": "♔", "1": "♕", "2": "♖", "3": "♗", 
    "4": "♘", "5": "♙", "6": "♚", "7": "♛", "8": "♜", "9": "♞",
    #special characters start here
    "!": "♟", "@": "♤", "#": "♠", "$": "♧", "%": "♣",
     "^": "♡", "&": "♥", "*": "♢","(": "♦", ")": "♩",
     ".": "♪", "?": "♫"
}


#precondition: a string that has been passed through the
#transposition and shift_and_wrap functions
#postcondition: applies mapping to the encrypted word
def apply_substitution(encrypted_word):
     
    substituted_word = ''.join(mapping.get(char, char) for char in encrypted_word)

    return substituted_word

#precondition: a string that has been encrypted before
#using the mapping dictionary on the first lines
#postcondition: applies reverse mapping to the encrypted word
def apply_reversed_substitution(encrypted_word):
     
     reversed_mapping = {v : k for k, v in mapping.items()}

     reversed_substituted_word = ''.join(reversed_mapping.get(char, char) for char in encrypted_word)

     return reversed_substituted_word

#precondition: none
#postcondition: reverses the order of the string
def transpose(text):
     return ''.join(reversed(text.strip()))

#precondition: a text file and a key (integer key for shifting)
#postcondition: function iterates through the text and determines if character is a special character, number, or letter
#it then shifts the letters depending on the character, and then keeps it in the range of 0-25 using modulo
#afterwards, returns the encrypted text shifted and wrapped
def shift_and_wrap(text, key):

    encrypted_text = ""

    for char in text:
        if char.isalpha(): #if a letter

            if char.isupper(): #if uppercase
                number = ord(char)
                #print(char, " is the number: ", number)

                #shift and wrap
                number = (ord(char) - ord('A') - key) % 26 + ord('A')

                #print(char, " is the number: ", number)

                encrypted_text += chr(number)

            elif char.islower(): #if lowercase
                number = ord(char)
                #print(char, " is the number: ", number)

                #shift and wrap
                number = (ord(char) - ord('a') - key) % 26 + ord('a')

                encrypted_text += chr(number)

                #print(char, " is the number: ", number)
            else: #if not an upper or lowercase
                encrypted_text += char
        elif char == " ":
                encrypted_text += " "
        elif char == '\n':
                encrypted_text += '\n'
        elif char == '\t':
                encrypted_text += '\t'
        else:
            encrypted_text += char

    return encrypted_text

#precondition: a text file and a key (integer key for shifting)
#postcondition: function iterates through the text and determines if character is a special character, number, or letter
#it then shifts the letters depending on the character, and then keeps it in the range of 0-25 using modulo
#afterwards, returns the decrypted text shifted and wrapped
def shift_and_wrap_decrypted(text, key):

    encrypted_text = ""

    for char in text:
        if char.isalpha(): #if a letter

            if char.isupper(): #if uppercase
                number = ord(char)
                #print(char, " is the number: ", number)

                #shift and wrap
                number = (ord(char) - ord('A') + key) % 26 + ord('A')

                #print(char, " is the number: ", number)

                encrypted_text += chr(number)

            elif char.islower(): #if lowercase
                number = ord(char)
                #print(char, " is the number: ", number)

                #shift and wrap
                number = (ord(char) - ord('a') + key) % 26 + ord('a')

                encrypted_text += chr(number)

                #print(char, " is the number: ", number)
            else: #if not an upper or lowercase
                encrypted_text += char
                
        elif char == " ":
                encrypted_text += " "
        elif char == '\n':
                encrypted_text += '\n'
        elif char == '\t':
                encrypted_text += '\t'
        else:
            encrypted_text += char
            
            

    return encrypted_text
    

#precondition: a string plain text and a user inputted key (integer)
#postcondition: returns a string of the text now, transposed, shifted and wrapped, and substituted (and encrypted)
def encryption(text, key):
    print("In Encryption, Text Is: ", text)

    transpose_texxt = transpose(text)

    print("After Transposing: ", transpose_texxt)

    encrypted_texxt = shift_and_wrap(transpose_texxt, key)

    print("After Shifting and Wrapping: ", encrypted_texxt)

    substituted_encrypted_text = apply_substitution(encrypted_texxt)

    print("After Applying Substitution: ", substituted_encrypted_text)

    return substituted_encrypted_text

#precondition: a string decrypted text that was encrypted with the same algoritm and a user inputted key (integer)
#postcondition: returns a string of the encrypted text now decrypted transposed, shifted and wrapped, and substituted
def decryption(text, key):
    print("In Decryption, Text Is: ", text)

    reversed_substituted_text = apply_reversed_substitution(text)
    print("After Reversing Substitution: ", reversed_substituted_text)

    decrypted_text = shift_and_wrap_decrypted(reversed_substituted_text, key)
    print("After Shifting and Wrapping: ", decrypted_text)

    reverse_transpose_text = transpose(decrypted_text)
    print("After Transposing: ", reverse_transpose_text)

    return reverse_transpose_text


    
#precondition: input_file: a text file with plain english words/special characters/numbers
#precondtition: output_file: a name to write out the output file with the encrypted text input_file
#precondition: key: an integer that the user inputed
def encrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
 
        with open(output_file, 'w') as file:
            for line in lines:
                file.write(encryption(line, key))
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
 
def decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
 
        with open(output_file, 'w') as file:
            for line in lines:
                file.write(decryption(line, key))
    except FileNotFoundError:
        print(f"Error: {input_file} not found!")
 
if __name__ == "__main__":
    print("0211243456")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
 
    choice = int(input("Choice: "))
    input_file = input("Enter the input file name: ")
    output_file = input("Enter the output file name: ")
    key = int(input("Enter the encryption/decryption key (integer): "))
 
    if choice == 1:
        encrypt_file(input_file, output_file, key)
    elif choice == 2:
        decrypt_file(input_file, output_file, key)
    else:
        print("Invalid choice")
    
