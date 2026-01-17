import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
''' #simple level
password=" "
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for letter in range(1,nr_letters+1):
   password+=random.choice(letters)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(1,nr_symbols+1):
    password+=random.choice(symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(1,nr_symbols+1):
    password+=random.choice(numbers)

print(password)
'''
#Hard level
pass_list=[]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
for letter in range(1,nr_letters+1):
   pass_list.append(random.choice(letters))

nr_symbols = int(input(f"How many symbols would you like?\n"))
for symbol in range(1,nr_symbols+1):
    pass_list.append(random.choice(symbols))

nr_numbers = int(input(f"How many numbers would you like?\n"))
for number in range(1,nr_symbols+1):
    pass_list.append(random.choice(numbers))

print(pass_list)
random.shuffle(pass_list)
print(pass_list)
password=" "
for char in pass_list:
    password+=char

print(f"your  password is: {password}")

