import random 
import string

chars = string.ascii_letters + string.digits + string.punctuation
print("PHOENIX PYTHON PASSWORD GENERATOR")
num = int(input("Enter The Number Of Passwords::"))
lenpass = int(input("Enter Length Of Password(s)::"))
for i in range(num):
    passwords=''
    for j in range(lenpass):
        passwords+=random.choice(chars)
    print(f"=========PASSWORD {i+1}============")
    print(passwords)