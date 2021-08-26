import random
what = input("What is this password for:")
pwd_len = int(input("Enter lengt of password:"))

s="abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ@#!&%"

pwd = "".join(random.sample(s,pwd_len))

print("Your password:",pwd)

with open('password.txt','a') as f:
    data = what+'\n'+pwd+'\n\n'
    f.write(data)
    f.close()
