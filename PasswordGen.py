import random
run = True
ALPHABET = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] 
def randomChar():
    return ALPHABET[random.randint(0,25)]
    
def Password_Gen():
    
    length = 3
    randomWord =""
    while length < 4:
        length = int(input("How long would you like the password to be? (Must be over 4): "))
        
    
    randomNum = str(random.randint(100,999))
    for character in range (length-3):
        randomWord += randomChar()
        
    randomWord += randomNum
    print(randomWord)       
        
while run == True:
    Password_Gen()
    q = input("Run Again? (y/n): ")
    if (q == "n"):
        run = False
    
