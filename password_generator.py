import random
import string

chars_lowercase = "abcdefghijklmnopqrstuvwxyz"
chars_uppercase = "aABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars_numbers = "0123456789"
chars_specialChars = "a@#$%^&*"

all_chars = chars_lowercase + chars_uppercase + chars_numbers + chars_specialChars

while True :
    length = int(input("Enter length of password (min. 4 chars and max. 15 chars) : "))
    
    if(length < 4) : 
        print("Enter min. length of 4")
    elif(length > 15) :
        print("Enter length of password less than 15")
    else : 
        break
    
password = []
    
password.append(random.choice(chars_lowercase))
password.append(random.choice(chars_uppercase))
password.append(random.choice(chars_numbers))
password.append(random.choice(chars_specialChars))
    
for i in range(length - 4) :
    password.append(random.choice(all_chars))
        
random.shuffle(password)
    
password = "".join(password)
    
print("Generated password : ", password)

    