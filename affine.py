#dictionary of the values corresponding to each letter of the alphabet
alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
#function to find the gcd of two numbers
def gcd(a,b):
    if a==0 or b== 0: return 0
    if a == b: return a
    if a > b: return gcd(a-b,b)
    return gcd(a,b-a)
#function to encrypt a message using the affine cipher
def affine():
    #asking for the plaintext to encrypt and the value for a
    plaintext = input("Provide the message you would like to encrypt")
    a = int(input("Provide a value for 'a'"))
    #checks if a is a valid number and if not asks for another value
    while gcd(a,26) != 1:
        a = int(input("Please provide a value for a that is coprime with 26"))
    #asks for a value for b
    b = int(input("Provide a value for 'b' between 0 and 26"))
    #checks if v is a valid number and if not asks for another value
    while b > 26:
        b = int(input("That value is not between 0 and 26. Please try again"))
    #output plaintext
    ciphertext = ""
    #encryption of the plaintext
    for char in plaintext:
        char = char.lower()
        if char == " ":
            ciphertext = ciphertext + " "
        else:
            newValue = alphabet[char]
            newValue = ((a * newValue) + b)
            if newValue > 26:
                newValue = newValue % 26
            for letter , value in alphabet.items():
                if value == newValue:
                    ciphertext = ciphertext + str(letter)
    return ciphertext

print(affine())