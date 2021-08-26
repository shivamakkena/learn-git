import random
import string

def randomPswd():
    password = []
    for i in range(6):
        alpha = random.choice(string.ascii_letters)
        digits = random.choice(string.digits)
        #password.append(alpha)
        password.append(digits)

    pwd=''.join(str(x) for x in password)
    print(pwd)
    
    
randomPswd()
