import random
print("PHOENIX PYTHON GENERATOR")
chars = "QWERTYUIOP[]ASDFGHJKL;\ZXCVBNM/asdfghjklqwertyuiopzxcvbnm&%$#@"
num=int(input("Enter the number of passwords:"))
lenofpass=int(input("Enter the length of the password(s):"))
print("Here are your passwords")
for pwd in range(num):
    passwords=''
    for i in range(lenofpass):
        passwords += random.choice(chars)
    print(f"===============PASSWORD {pwd}================")
    print(passwords)
    print("========================================")