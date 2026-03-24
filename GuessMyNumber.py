# import random

# password = random.randint(1,100)
# score = 0
# trials = 3

# for i in range(trials):
#     guess = int(input("Guess the password(1 to 100):"))
#     if password == guess:
#         print("Hooray! You got it!")
#         break
#     else:
#         print("Try Again.")

# print("Game Over!")


#Ask the user to enter a password.
# Allow a maximum of 3 attempts.
# If the correct password is entered, print “Access Granted” and stop the loop immediately.
# If all attempts are used, print “Access Denied”.

# password = "8052"
# trials = 3
# for i in range(trials):
#     guess = str(input("Enter Password:"))
#     if password == guess:
#         print("Access Granted!")
#         break
#     else:
#         print("Try Again!")
# else:
#  print("Access Denied!")


# Write a program that prints numbers from 1 to 50.

# If a number is divisible by 3 → print "Fizz"

# If a number is divisible by 5 → print "Buzz"

# If a number is divisible by both 3 and 5 → print "FizzBuzz"

# Otherwise → print the number itself

# Ask the user to guess a secret word.
# Keep asking until they type the correct word.
# Stop the loop when they get it right.



# word = "Printer"
# trials = 3
# for i in range(trials):
#      guess = str(input("Guess The Secret Word:"))
#      if word == guess:
#          print("Access Granted!")
#          break
#      else:
#          print("Try Again!")
# else:
#     print("Access Denied!")


for i in range(1,51):
    if i % 3 ==0 and i % 5==0:
     print("FizzBuzz")
     continue
    elif i % 5 ==0:
     print("Buzz")
     continue
    elif i % 3 ==0:
     print("Fizz")
     continue
    print(i)