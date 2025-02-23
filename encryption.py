pokemon_list_letters = [ #for letters a - z
    "Ampharos", "Dragonite", "Gyrados", "Bronzong", "Vilepume", "Latios",
    "Blastoise", "Mimkyu", "Ho-Oh", "Quagsire", "Wooper", "Gengar",
    "Ambipom", "Uxie", "Onix", "Dragapult", "Cinderance", "Squirtle",
    "Yveltal", "Goodra", "Talonflame", "Aegislash", "Hydreigon", "Staraptor",
    "Sceptile", "Poliwrath"
]

pokemon_list2 = [ #for numbers 0-9
    "Bidoof", "Lanturn", "Sentret", "Dunsparce", "Hypno", 
    "Darkrai", "Starmie", "Xatu", "Bellsprout", "Bishop"
]

pokemon_list3 = [ #for special characters !@#$%^&*().?
     "Metapod", "Seedot", "Trapinch", "Spiritomb", "Buzzwole",
     "WalkingWake", "Skeledirge", "Avalugg", "Landorous", "Seismitoad",
     "Throh", "Sawk"
]

def transpose(text):
    return text[::-1]

def shift_and_wrap():
    print("hello")
    

def encryption(text, key):
    #encrypted_text = ''.join([chr(ord(char) + key) for char in text])
    
    encrypted_text = " "



    
    

    special_characters = set('!@#$%^&*().?')

    if any(s_char in special_characters for s_char in text):
        print("special character: ")
    

    for char in text:
        if char.isalpha(): #if a letter
            number = ord(char)
            print(char, " is the number: ", number)

            #applying a shift and a wrap
            number = (number - key) % 26

            print(char, " is the number: ", number)


        elif char.isdigit(): #if char is a number
            #should i just convert numbers to letters? since i am using letters to numbers? 
            print(char, " is a number")

            #applying a shift

            print(char, " is now the char: ")

        elif char == " ":
            print("space")

        elif any(char in special_characters for char in text):
            character_number = ord(char)
            print(char, " number is now: ", character_number)

        else:
            print(" unknown character: ", char)

 
    return encrypted_text
 
def decryption(text, key):
    decrypted_text = ''.join([chr(ord(char) - key) for char in text])
    return decrypted_text
 
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
    print("01")
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
