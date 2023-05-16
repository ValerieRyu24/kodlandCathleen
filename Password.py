import random
element = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
panjang_password = int(input("Passwordnya mau sampai berapa karakter?"))

password = ''
for i in range(panjang_password):
    password += random.choice(element)
print(password)