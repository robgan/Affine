alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
#function to encode a message using the vigenere cipher
def vigenere():
    
    plaintext = input("Provide the message you would like to encrypt")
    keyword = input("Provide a keyword")
    
    ciphertext = ""
    keywordCounter = 0
    for i in range(len(plaintext)):
        print(i)
        char = plaintext[i].lower()
        if char == " ":
            ciphertext = ciphertext + " "
        else:
            value = alphabet[char]
            print(keyword[keywordCounter % len(keyword)])
            keywordValue = alphabet[keyword[keywordCounter % len(keyword)]]
            newValue = (value+keywordValue) % 26
            for letter,value in alphabet.items():
                if value == newValue:
                    ciphertext = ciphertext + str(letter)
            keywordCounter += 1
    return ciphertext

print(vigenere())