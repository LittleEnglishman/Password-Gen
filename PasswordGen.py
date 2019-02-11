import random
def Password_Gen():
    ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
    length = 3
    randomWord =""
    while length < 4:
        length = int(input("How long would you like the password to be? "))
        
    
    randomNum = str(random.randint(100,999))
    for character in range (length-3,random.randint(4,10)):
        randomWord += str(ALPHABET[random.randint(1,26)])
        
    randomWord += randomNum
    print(randomWord)
        
Password_GEN()
