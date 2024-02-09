import math
import string

#Q1. Write a function to calculate volume of a sphere
def volume_sphere(r):
    return (4/3) * math.pi * (r**3)


#Q2. Write a function that checks whether a number is in given range (inclusive of high and low)
def check_range(num,low,high):
    return num in range(low,high+1)

#Q3. Write a function that accepts a string and counts number of lowercase letters and uppercase letters
def count_lower_upper(word):
    Upper_count = 0
    lower_count = 0
    for i in word:
        if ord(i) >= 65 and ord(i) <= 91:
            Upper_count+=1
        elif ord(i) >= 97 and ord(i) <= 122:
            lower_count+=1
    
    print(Upper_count)
    print(lower_count)

#Q4. write a function that takes a list and returns a new list with unique elements of the first list
    
def unique_list(nums):
    return list(set(nums))

#Q5. Write a function to multiply all elements of list
def multiply_list(nums):
    ans = 1
    for i in nums:
        ans*=i
    return ans

#Q6. write a function to check whether a string is a palindrome
def check_palindrome(word):
    return word == word[::-1]


#Q7 Write a function to check whether a string is pangram 
def check_pangram(word):
    alphabets = list(string.ascii_lowercase)

    for i in word:
        if i in alphabets:
            alphabets.remove(i)
    
    return alphabets == []

print(check_pangram("The quick brown fox jumps over the lazy dog"))