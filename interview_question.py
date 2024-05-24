# You have a text. Write a program to find the most repeated character in the text

# Algorithm:

# 1. What kind of data structure is needed to store the number of times a character is present in the string? Dictonary. 
from pprint import pprint
char_frequency = {}
sentence = "This is a common interview question"

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1
pprint(char_frequency,width=1)

# We found the frequency of each character but we need to sort in the descending order in order to find the characater with the highest frequency. So, we will convert the dictionary into a list via a tuple

# print(sorted(char_frequency.items())) #.items returns all key value pairs as list of tuples, but since tuple doesn't know what to sort, we need to convert it into a list


# We should pass the second argument to sorted function. 

char_frequency_sorted = sorted(char_frequency.items(), 
                               key=lambda kv:kv[1], 
                               reverse=True)

print("Answer: ", char_frequency_sorted[0])