letter_list = [ #for letters a - z
    "♬", "♭", "♮", "♯", "°", "ø",
    "؂", "≠", "≭", "☧", "☨", "☩",
    "☫", "☬", "☭", "☯", "☽", "☾",
    "✙", "✛", "✜", "✝", "✞", "✟",
    "‡", "♁"
]

numbers_list = [ #for numbers 0-9
    "♔", "♕", "♖", "♗", "♘", 
    "♙", "♚", "♛", "♜", "♞"
]

special_characters_list = [ #for special characters !@#$%^&*().?
     "♟", "♤", "♠", "♧", "♣",
     "♡", "♥", "♢", "♦", "♩",
     "♪", "♫"
]

def apply_substitution():
     

     
     print("hello")


def transpose(text):
    return text[::-1]

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
    transpose_texxt = transpose(text)

    encrypted_texxt = shift_and_wrap(transpose_texxt, key)

    return encrypted_texxt

 
def decryption(text, key):
    reverse_transpose_text = transpose(text)

    decrypted_texxt = shift_and_wrap_decrypted(reverse_transpose_text, key)

    return decrypted_texxt


    
 
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
    print("02112434")
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
