alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

def hill():
    plaintext = input("Provide the message you would like to encrypt")
    keyword = input("Provide the keyword you would like to use to encode")
    
    print (keyword)
    keywordArray = [[-1,-1],[-1,-1]]
    i = 0
    for j in range (len(keywordArray[0])):
        for k in range (len(keywordArray[1])):
            keywordArray[j][k] = alphabet[keyword[i]]
            i += 1
    print (keywordArray)
    
    ciphertext = ""
    for char in range(len(plaintext)):
        char = char.lower()
        if char == " ":
            ciphertext = ciphertext + " "
        else:
            
        
            
        
hill()