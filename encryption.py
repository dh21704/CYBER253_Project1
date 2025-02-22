pokemon_list_letters = [ #for letters a - z
    "Ampharos", "Dragonite", "Gyrados", "Bronzong", "Vilepume", "Latios",
    "Blastoise", "Mimkyu", "Ho-Oh", "Quagsire", "Wooper", "Gengar",
    "Ambipom", "Uxie", "Onix", "Dragapult", "Cinderance", "Squirtle",
    "Yveltal", "Goodra", "Talonflame", "Aegislash", "Hydreigon", "Staraptor",
    "Sceptile", "Poliwrath"
    ]

pokemon_list2 = [ #for numbers 0-9
    "Bidoof", "Lanturn", "Sentret", "Dunsparce", "Hypno", 
    "Darkrai", "Starmie", "Xatu", "Bellsprout"
]


def encryption(text, key):
    #encrypted_text = ''.join([chr(ord(char) + key) for char in text])
    
    encrypted_text = " "

    for char in text:
        if char.isalpha(): #if a letter
            number = ord(char)
            print(char, " is the number: ", number)
        elif char.isdigit(): #if char is a number
            print(" ")
        elif char == " ":
            print(" space ")
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
