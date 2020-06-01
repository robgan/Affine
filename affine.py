alphabet = {"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}

def gcd(a,b):
    if a==0 or b== 0: return 0
    if a == b: return a
    if a > b: return gcd(a-b,b)
    return gcd(a,b-a)
    


def affine():
    message = input("Provide the message you would like to encrypt")
    a = int(input("Provide a value for 'a'"))
    print (gcd(a, 26))    
    while gcd(a,26) != 1:
        a = int(input("Please provide a value for a that is coprime with 26"))
    b = int(input("Provide a value for 'b' between 0 and 26"))
    while b > 26:
        b = int(input("That value is not between 0 and 26. Please try again"))
    newMessage = ""
    for char in message:
        char = char.lower()
        if char == " ":
            newMessage = newMessage + " "
        else:
            newValue = alphabet[char]
            newValue = ((a * newValue) + b)
            if newValue > 26:
                newValue = newValue % 26
            for letter , value in alphabet.items():
                if value == newValue:
                    newMessage = newMessage + str(letter)
    return newMessage

print(affine())