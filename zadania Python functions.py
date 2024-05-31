#-------------------------------------------------------------------------------
#Python functions - zadania

#1. Write a Python function to find the maximum of three numbers.
"""
def max_of_three_numbers(num_list):
  max_num = max(num_list)
  return max_num

list_of_numbers = [1, 7, 4]
print(max_of_three_numbers(list_of_numbers))
"""

#2. Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
"""
def sum_numbers(num_list):
  sum_of_numbers = sum(num_list)
  return sum_of_numbers

list_of_numbers = [1, 5, 7, 4, 0]
print(sum_numbers(list_of_numbers))
"""

#3. Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336
"""
def multiply_numbers(num_list):
  result = 1
  for i in num_list:
    result = result * i
  return result

list_of_numbers = [1, 4, 2, 7, 9, 5, -1]
print(multiply_numbers(list_of_numbers))
"""

#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"
"""
def rev_string(string):
  return string[::-1]

string_to_rev = "Trawa jest skoszona"
print(rev_string(string_to_rev))
"""

#5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""
def calc_fact_num(number):
  fact_num = 1
  if number > 0:
    for i in range(1, number+1):
      fact_num = fact_num * i
    return fact_num
  else:
    return fact_num
number = 5
print(calc_fact_num(number))
"""

#6. Write a Python function to check whether a number falls within a given range.
"""
def num_in_range(number):
  if number in range(1, 10):
    return "Number falls within a given range"
  else:
    return "Number doesn't fall within a given range"
number = 6
print(num_in_range(number))
"""

#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12
"""
def count_upp_and_low_case_letters(string):
  d = {"Upper_Case": 0,"Lower_Case": 0}
  for i in string:
    if (i.isupper()):
      d["Upper_Case"] += 1
    elif (i.islower()):
      d["Lower_Case"] += 1
    else:
      pass

  print("No. of Upper case characters: ", d["Upper_Case"])
  print("No. of Lower case Characters: ", d["Lower_Case"])

given_string = "Wiersz autorstwa Juliana Tuwima"
print("Original given string: ", given_string)
count_upp_and_low_case_letters(given_string)
"""

#8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
"""
def unique_elements(input_list):

    return list(set(input_list))

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_elements(sample_list))
"""

#9. Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.
"""
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(4))
"""

#10. Write a Python program to print the even numbers from a given list.
#Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected Result : [2, 4, 6, 8]
"""
def even_numbers(input_list):
    return [num for num in input_list if num % 2 == 0]

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_numbers(sample_list))
"""

#11. Write a Python function to check whether a number is "Perfect" or not.
#According to Wikipedia : In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum). Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
#Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.
"""
def is_perfect(number):
    if number < 1:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

print(is_perfect(6))
print(is_perfect(28))
"""

#12. Write a Python function that checks whether a passed string is a palindrome or not.
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
"""

#13. Write a Python function that prints out the first n rows of Pascal's triangle.
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
"""
def pascals_triangle(n):
    result = []
    for i in range(n):
        row = [1]
        if result:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        result.append(row)
        print(row)

pascals_triangle(5)
"""

#14. Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
"""
import string

def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(s.lower())

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hello world"))
"""

#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow
"""
def sort_hyphenated_sequence(sequence):
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

sample_sequence = "green-red-yellow-black-white"
print(sort_hyphenated_sequence(sample_sequence))
"""

#16. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).
"""
def squares_list():

    return [i ** 2 for i in range(1, 31)]

print(squares_list())
"""

#17. Write a Python program to create a chain of function decorators (bold, italic, underline etc.).
"""
def bold(func):
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

def underline(func):
    def wrapper(*args, **kwargs):
        return "<u>" + func(*args, **kwargs) + "</u>"
    return wrapper

@bold
@italic
@underline
def text(message):
    return message

print(text("Hello World"))
"""

#18. Write a Python program to execute a string containing Python code.
"""
code = """
"""
def add(a, b):
    return a + b

result = add(5, 3)
"""
"""
exec(code)
print(result)  # Wydrukuje: 8
"""

#19. Write a Python program to access a function inside a function.
"""
def outer_function():
    def inner_function():
        return "Wewnętrzna funkcja"
    return inner_function

inner = outer_function()
print(inner())
"""

#20. Write a Python program to detect the number of local variables declared in a function.
#Sample Output:
#3
"""
def sample_function():
    a = 1
    b = 2
    c = 3
    return a + b + c

print(sample_function.__code__.co_nlocals)  # Wydrukuje: 3
"""

#21. Write a Python program that invokes a function after a specified period of time.
#Sample Output:
#Square root after specific miliseconds:
#4.0
#10.0
#158.42979517754858
import time

def delayed_execution(func, delay, *args, **kwargs):
    time.sleep(delay)
    return func(*args, **kwargs)

# Przykład użycia
import math
result = delayed_execution(math.sqrt, 2, 16)
print(result)  # Wydrukuje: 4.0 po 2 sekundach



