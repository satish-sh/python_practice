# ------------>    PROGRAM - 01   <------------------------

# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

""" input_str = input("enter the string:")
dimentions = [int(x) for x in input_str.split(",")]

row_num = dimentions[0]
col_num = dimentions[1]

array = []

for i in range(row_num):
    row=[]
    for j in range(col_num):
        mul = i*j
        row.append(mul)
    array.append(row)

print(array)   """


# ------------>    PROGRAM - 02   <------------------------

# Write a program that accepts a sentence
# calculate the number of letters (upper case letters and lower case letters)and digits.
""" 
sentence = input("enter the sentence : ")

dl = {"digits": 0, "cap_letters": 0, "small_letters": 0}
for each in sentence:
    if each.isdigit():
        dl["digits"] += 1

    elif each.isalpha():
        if each.isupper():
            dl["cap_letters"] += 1
        else:
            dl["small_letters"] += 1

    else:
        pass

cap_letters = dl["cap_letters"]
small_letters = dl["small_letters"]
digits = dl["digits"]

print(f"cap_letters: {cap_letters}, small_letters: {small_letters}, digits: {digits}") """


# ------------>    PROGRAM - 03  <------------------------

# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.

""" 
input_numbers = input("enter the numbers")
square_of_input = [int(x)**2 for x in input_numbers.split(",") if int(x)%2 != 0]

print(square_of_input) """


# ------------>    PROGRAM - 04   <------------------------

# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
# Passwords that match the criteria are to be printed, each separated by a comma.
""" import re
passwords = input("Please enter the passwords :").split(",")

checked_password = []
for password in passwords:
    if len(password) <6 or len(password) > 12 :
        continue
    else:
        pass

    if not re.search("[a-z]", password):
        print(password +"d")
        continue
    elif not re.search("[0-9]", password):
        print(password + "dd")
        continue
    elif not re.search("[A-Z]", password):
        print(password + "ddd")
        continue
    elif not re.search("[$#@]", password):
        print(password)
        continue
    else:
        pass
    
    checked_password.append(password)

print(checked_password) """


# ------------>    PROGRAM - 05   <------------------------

class DivisibleBySeven:
    def __init__(self, n):
        self.n = n
    
    def divisible_by_seven(self):
        for num in range(0, self.n + 1):
            if num % 7 == 0:
                return num

# Example usage
n = 50
div7 = DivisibleBySeven(n)

# Iterate over numbers divisible by 7
for number in div7.divisible_by_seven():
    print(number)
