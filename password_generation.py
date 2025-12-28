import random
letters = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|',
    ';', ':', "'", '"', ',', '.', '<', '>', '/', '?'
]
print("Welcome to PyPassword Generation!")
nr_letter = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_number = int(input("How many number would you like?\n"))
password = []
for i in range(nr_letter):
    password += random.choice(letters)
for i in range(nr_symbols):
    password += random.choice(symbols)
for i in range(nr_number):
    password += random.choice(numbers)
print("before shuffle:",password)
random.shuffle(password)
print("After shuffle",password)
pas = "".join(password)
print(f"Final password '{pas}'")