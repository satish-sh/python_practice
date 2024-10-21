# Palindrom or Not
""" num = input("Enter the Number : ")

left = 0
right = len(num) - 1
temp = True

while left < right:
    if num[left] != num [right]:
        temp = False

    left += 1
    right -= 1

if temp:
    print("Palindrome")

else:
    print("Not a Palindrome")
 """




# Armstrong number or not

""" def is_armstrong_number(num):
    digits = str(num)
    num_digits = len(digits)
    
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    
    return armstrong_sum == num

input_number = int(input("Enter a number: "))
if is_armstrong_number(input_number):
    print(f"{input_number} is an Armstrong number.")
else:
    print(f"{input_number} is not an Armstrong number.") """




# fibonacci series
""" nterms = int(input("how many terms : "))
n1, n2 = 0, 1
count = 0
if nterms < 0:
    print("please enter the positive number")

elif nterms == 1:
    print(f"fibonacci series : {n1}")

else:
    print("Fibonacci series : ")
    while count < nterms:
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth

        count += 1
 """




#  Check whether the given strings are anagrams or not.
""" def is_anagrams(string1, string2):
    temp = True
    for char in string1:
        if string1.count(char) == string2.count(char):
            temp = False
        

    return "Anagrams" if temp else "Not an anagram"

output = is_anagrams("listen", "silent")
print(output)
 """


# Longest Common Substring
""" def longest_common_substring(first, second):
    left = 0
    temp = ""
    longest = ""

    while left < len(first) and left < len(second):
        if first[left] == second[left]:
            temp += first[left]
        else:
            if len(temp) > len(longest):
                longest = temp
                temp = ""

        left = left + 1
    return longest


first = "qwerdfghh"
second = "qwedfggf"
result = longest_common_substring(first, second)

print(result) """

# print the Count the duplicates
def get_duplicates(list_a):
    dict_a = {}
    for each in list_a:
        dict_a[each] = dict_a.get(each, 0) + 1
    
    output = []
    for key, val in dict_a.items():
        if val > 1:
            output.append(key)
    return output

list_a = [1,2,3,2,4,5,6,6]
result = get_duplicates(list_a)
print(result)