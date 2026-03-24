# num1 = int(input("Enter 1st number:"))
# operator = input("Enter operator:")
# num2 = int(input("enter 2nd number:"))

# if operator == "+":
#  add = num1 + num2
#  print("Addition:",add)


# def greet(name):
#     print("Hello",name,"how are you doing?")
#     print("It is nice to meet you.")
#     print("What can I do for you?")

# greet("Daniel")
# greet("Andreas")
# greet("Logan")
# greet("Jacob")
# greet("Aiden")
# greet("Danstan")
# greet("Brayden")
# greet("Ben")
# greet("Jabriel")

# def multiply(a,b):
#      multiply = a*b
#      print("Multiplication",multiply)


# multiply(2,3)
# multiply(5,7)

# def area_Rect(l,w):
#  area = l*w 
#  print("Area of the rectangle:",area)

# area_Rect(20,13)

# def Square(Number):
#   Square = Number*Number
#   print(Square)

# Square(8)

# create a function to do the following:
# a) multiplication of 2 numbers
# b) Area of a rectangle
# c) Square root of a number

names = ["Sebastian","Danstan","Jabriel","Daniel","Brayden","Aiden"]

print(names)

import random
name = random.choice(names)

print("Today's helper is:",name)

names.remove(name)

print(names)

# #accessing
# print(names[4])
# print(names[-1])


# #add(append)
# names.append("Benjamin","")



# #delete
# del names[-1]
#names.remove("Aiden")

# #change



# #looping operation
# for name in names:
#     print(name)

# name = input("Enter the name to search:")
# if name in names:
#     print(name,"found")

# else:
#     print(name,"not found")

# password = input("Enter your password:")

# print("length",len(password))


# import random
# name = random.randint(1,10)

#length of a list

# print("length",len(list))
# if (len(password)) >= 8:
#     print("Strong")

# else:
#     print("Weak")

password = input("Enter password:")
score = 0

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
for let in upper:
    if let in password:
        score +=2
        print(score)

lower = "qwertyuiopasdfghjklzxcvbnm"
for let in lower:
    if let in password:
        score +=1
        print(score)

symbol = "!@#$%^&*?+_=;'][<>]()"
for let in symbol:
    if let in password:
        score +=3
        print(score)

number = "1234567890"
for let in number:
    if let in password:
        score +=4

list = [upper,lower,symbol,number]

import random
import string

def generate_strong_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")
    
    upper = random.choice(string.ascii_uppercase)
    lower = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    password_chars = [upper,lower,digit,symbol]

    all_chars = string.ascii_letters + string.digits + string.punctuation

    for _ in range(length - 4):
        password_chars.append(random.choice(all_chars))


    random.shuffle(password_chars)
    password = ''.join(password_chars)

    return password

print("Generated Password:", generate_strong_password(12))
# Password Strength Checker
# Ask the user to enter a password.
# Check and print:
# "Strong" if length ≥ 8 and contains a number
# "Weak" otherwise
 
#  Random Name Picker
# Create a list of student names.
# Randomly select one name.
# Print:
# "Today’s helper is: <name>"

# Remove the chosen name so it is not picked again.