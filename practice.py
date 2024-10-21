# PROGRAM : 1
# list of numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number.

""" def find_numbers(numbers, target):
    left = 0
    right = len(numbers)-1
    result = []
    while left < right:
        total = numbers[left] + numbers[right]
        if target == total:
            result.append((numbers[left], numbers[right]))
            left += 1
            right += 1

        elif target < total:
            right -=1 
        
        else:
            left += 1
    
    return result

numbers = [1, 2, 3, 3, 4, 6]
target = 5
output = find_numbers(numbers, target)
print(*output) """



# PROGRAM : 2
# --------> if list is not sorted <-----------
""" def find_numbers_for_target(numbers, target):
    dict_a = {}
    result = []

    for number in numbers:
        compliment = target-number
        if compliment in dict_a and dict_a[compliment] != 0:  #-----> not to duplicate that are already paired
            result.append((compliment, number))
            dict_a[compliment] -= 1       # ----> decrease the count of number if that number paired in above line

        dict_a[number] = dict_a.get(number,0) + 1
    return result

numbers = [1, 6, 3, 2, 4, 3]         # example i/p ---> [1, 6, 3, 2, 4, 4, 3] , [1, 6, 3, 2, 2, 4, 4, 3] 
target = 6                                             
output = find_numbers_for_target(numbers, target)
print(output) """

# PROGRAM : 3
# Given an array A of strings made only from lowercase letters, 
# Return a list of all characters that show up in all strings within the list (including duplicates).  
# For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

""" def chars_in_all_strings(strings):
    comp_dict = {}
    result = []

    # count the frequency of each character in first string
    for char in strings[0]:
        comp_dict[char] = comp_dict.get(char, 0) + 1
    
    #compare remaining strings with first string and update frequency of characters. 
    for i in range(1, len(strings)):
         for key in list(comp_dict.keys()):
            if key in strings[i]:
                char_count = min(strings[i].count(key), comp_dict[key])
                comp_dict[key] = char_count
            
            else:
                del comp_dict[key]

    for key, val in comp_dict.items():````
        result.extend([key] * val)``
    
    return result


list_a = ["bella","label","roller"]
output = chars_in_all_strings(list_a)
print(output)
 """



# PROGRAM : 4
# Counting Occurrences of a Substring

""" def count_substring(strings, sub_string):
    count = 0
    for string in strings:
        count += string.count(sub_string)
    return count

string_list = ["hello world", "hello there", "hi there", "world"]
string_to_count = "hello"
result = count_substring(string_list, string_to_count)
print(result) """
