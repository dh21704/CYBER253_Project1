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


def apply_substitution(encrypted_word):
     
    substituted_word = ''.join(mapping.get(char, char) for char in encrypted_word)

    return substituted_word

def apply_reversed_substitution(encrypted_word):
     
     reversed_mapping = {v : k for k, v in mapping.items()}

     reversed_substituted_word = ''.join(reversed_mapping.get(char, char) for char in encrypted_word)

     return reversed_substituted_word


def transpose(text):
     return ''.join(reversed(text.strip()))

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
    

def encryption(text, key):
    print("In Encryption, Text Is: ", text)

    transpose_texxt = transpose(text)

    print("After Transposing: ", transpose_texxt)

    encrypted_texxt = shift_and_wrap(transpose_texxt, key)

    print("After Shifting and Wrapping: ", encrypted_texxt)

    substituted_encrypted_text = apply_substitution(encrypted_texxt)

    print("After Applying Substitution: ", substituted_encrypted_text)

    return substituted_encrypted_text

 
def decryption(text, key):
    print("In Decryption, Text Is: ", text)

    reversed_substituted_text = apply_reversed_substitution(text)
    print("After Reversing Substitution: ", reversed_substituted_text)

    decrypted_text = shift_and_wrap_decrypted(reversed_substituted_text, key)
    print("After Shifting and Wrapping: ", decrypted_text)

    reverse_transpose_text = transpose(decrypted_text)
    print("After Transposing: ", reverse_transpose_text)

    return reverse_transpose_text


    
 
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
