alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

def caesar():
    #message that is going to be encrypted
    plaintext = input("Provide the message you would like to encrypt")
    #how much the message will be shifted by
    a = int(input("How much would you like to shift the message by?"))
    #checks if the value is more than 26
    while a > 26:
        a = int(input("Please provide a value between 0 and 26"))
    ciphertext = ""
    #encryption of the plaintext
    for char in plaintext:
        char = char.lower()
        if char == " ":
            ciphertext = ciphertext + " "
        else:
            newValue = alphabet[char] + a
            for letter,value in alphabet.items():
                if value == newValue:
                    ciphertext = ciphertext + str(letter)
                    
    return ciphertext

print(caesar())

