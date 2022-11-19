
def encrypt(message, key):
    string = ""
    for letter in message:
        index = int(ord(letter)) + key
        if index > 122:
            index -= 26

        string += chr(index)
    return string

def decrypt(message, key):
    string = ""
    for letter in message:
        index = int(ord(letter)) - key
        if index < 97:
            index += 26
        string += chr(index)
    return string

def brute(message):
    count = 0
    while count <= 25:
        output = decrypt(message, count)
        count += 1
        print (f"{count} {output}")
    

choice = input("Do you wish to encrypt or decrypt a message: ")

if choice == "encrypt":
    MESSAGE = input("Enter your message: ")
    KEY = int(input("Enter the key number (1-26): "))
    output = (encrypt(MESSAGE, KEY))
    print("Your translated text is:")
    print(f"{output}")

elif choice == "decrypt":
    MESSAGE = input("Enter your message: ")
    KEY = int(input("Enter the key number (1-26): "))
    output = (decrypt(MESSAGE, KEY))
    print("Your translated text is:")
    print(f"{output}")

elif choice == "brute":
    MESSAGE = input("Enter your message: ")
    output = brute(MESSAGE)
    
else:
    print("invalid choice run again")
    
          


        
        
        
        
