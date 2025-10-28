# import the math module to access mathematical functions and constants
import math
import random

# constants from the math module
a = math.pi
b = math.e
print(a) # 3.141592653589793
print(b) # 2.718281828459045

# using math functions
c = math.fabs(-7.25)  # absolute value
print(c) # 7.25
d = math.ceil(3.9)  # ceiling value: smallest integer >= x
print(d) # 4
e = math.floor(3.9)   # floor value: largest integer <= x
print(e) # 3
f = math.pow(2, 3)    # power function: 2 raised to the power of 3
print(f) # 8.0
g = math.sqrt(16)   # square root
print(g) # 4.0

# random numbers: don't forget to import random module
a = random.random()
print(a) # random float between 0.0 and 1.0
b = random.randint(1, 10)  # random integer between 1 and 10
print(b) # e.g., 7

c = random.uniform(1.5, 5.5)  # random float between 1.5 and 5.5
print(c) # e.g., 3.6789
d = random.sample(range(1, 100), 5)  # 5 unique random numbers from 1 to 99
print(d) # e.g., [23, 45, 67, 12, 89]

e = random.choice(['apple', 'banana', 'cherry'])  # random choice from
print(e) # e.g., 'banana'

num_list_1 = [1, 2, 3, 4, 5]
random.shuffle(num_list_1)
print(num_list_1) # e.g., [1, 4, 2, 5, 3]

num_list_2 = [10, 20, 30, 40, 50]
shuffled_list = random.sample(num_list_2, len(num_list_2)) # len() to get the length of the list: we will get 'len()' number of elements from the list, then put it into a new list with random order. each element will only appear once.
print(num_list_2) # Original list: [10, 20, 30, 40, 50]
print(shuffled_list) # e.g., [30, 10, 50, 20, 40]



# --- This is a horizontal line for separation ---

# string methods
str = "Hello"
print(len(str))  # length of string; prints 5
print(str[1]) # access character by index; prints 'e'
print(str.index("l"))  # get the first index of character; prints 2; raises 'ValueError: substring not found' if not found
print(str.find("l"))  # find the first index of character; prints 2; returns '-1' if not found

print(str.upper())  # convert to uppercase; prints 'HELLO'
print(str.lower())  # convert to lowercase; prints 'hello'
print(str.capitalize())  # capitalize first letter; prints 'Hello'

print(str.startswith("He"))  # check if string starts with substring; prints True
print(str.endswith("lo"))  # check if string ends with substring; prints True

print(str.split("e"))  # split string by character; prints ['H', 'llo']
print(str.strip("H"))  # remove leading/trailing characters; prints 'ello'

print(str.count("l"))  # count amount of character; prints 2
print(str.join(["H", "e", "l", "l", "o"]))  # join list into string with separator; prints 'HHelloeHellolHellolHelloo' -> 'H' + 'str' + 'e' + 'str' + 'l' + 'str' + 'l' + 'str' + 'o'
print("".join(["H", "e", "l", "l", "o"]))  # join list into string without separator; prints 'Hello'
print(str.replace("H", "J"))  # replace character; prints 'Jello'

str2 = "World"
print(f"{str} {str2}!") # prints "Hello World!"
str3 = str + str2
print(str3) # prints "HelloWorld"

str3 = str2[0:2] # slicing string from index 0 to 2 (not including index 2)
print(str3) # prints "Wo"

str = "\"Hello World\"" # use backslash to transfer special characters
print(str) # prints ""Hello World""

str2 = "Hello\nWorld" # use \n to create a new line
print(str2) # prints "Hello
            #          World"

name_list = ["Alex", "Bob", "Cathy"]
age_list = [23, 25, 27]
height_list = [1.65, 1.72, 1.76]

# this is old style string formatting:
# Hello Alex,23,1.650000
# Hello Bob,25,1.720000
# Hello Cathy,27,1.760000
for i in range(len(name_list)):
    str = "Hello %s,%d,%f" %(name_list[i], age_list[i], height_list[i]) # %s for string, %d for integer, %f for float
    print(str)

# this is new style string formatting:
# Hello Alex, 23, 1.65
# Hello Bob, 25, 1.72
# Hello Cathy, 27, 1.76
for name, age, height in zip(name_list, age_list, height_list):
    print(f"Hello {name}, {age}, {height}")

# --- This is a horizontal line for separation ---

# list methods
list = [1, 2, 3, 4]
a = list[0] # access element by index
print(a) # prits 1
list.append(5)  # add element to the end
print(list) # prints [1, 2, 3, 4, 5]
list.insert(2, 2.5)  # insert element at index 2
print(list) # prints [1, 2, 2.5, 3, 4, 5]
list.remove(2.5)  # remove first occurrence of element
print(list) # prints [1, 2, 3, 4, 5]
print(len(list)) # get length of list; prints 5
print(min(list), max(list)) # get minimum and maximum value; prints 1 5

list_misordered = [3, 1, 4, 5, 2]
list_misordered.sort()  # sort list in ascending order
print(list_misordered) # prints [1, 2, 3, 4, 5]
list_misordered.sort(reverse=True)  # sort list in descending order
print(list_misordered) # prints [5, 4, 3, 2, 1]

list2 = [7, 8, 9]
print(f"{list}{list2}") # prints [1, 2, 3, 4, 5][7, 8, 9]
list3 = list + list2
print(list3) # prints [1, 2, 3, 4, 5, 7, 8, 9]

list4 = list2 * 3 # repeat the list 3 times
print(list4) # prints [7, 8, 9, 7, 8, 9, 7, 8, 9]

print(list4.count(7)) # count how many times 7 appears in the list; prints 3

print(list2.pop(1)) # # remove element at index 1 and return the element you removed; prints 8
print(list2) # prints [7, 9]; list2 is now modified by pop(1), the 8 is removed

# --- This is a horizontal line for separation ---

# tuple methods
tuple = (1, 2, 3, 4)
print(tuple[0]) # access element by index; prints 1
print(len(tuple)) # get length of tuple; prints 4
print(min(tuple), max(tuple)) # get minimum and maximum value; prints 1 4

# del tuple # delete the entire tuple
# print(tuple) # raises 'NameError: name 'tuple' is not defined' because the tuple has been deleted

print(tuple * 3) # repeat the tuple 3 times; prints (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

t1 = (5, 6, 7)
t2 = (8, 9)
t3 = tuple + t1 + t2
print(t3) # concatenate tuples; prints (1, 2, 3, 4, 5, 6, 7, 8, 9)

# --- This is a horizontal line for separation ---

# dictionary methods
dict = {"Alex": 23, "John": 25, "Cathy": 27}

print(dict["Alex"]) # access value by key; prints 23

dict["Bob"] = 30  # add new key-value pair
print(dict) # prints {'Alex': 23, 'John': 25, 'Cathy': 27, 'Bob': 30}

dict["Alex"] = 24  # update value for existing key
print(dict) # prints {'Alex': 24, 'John': 25, 'Cathy': 27, 'Bob': 30}

del dict["John"]  # delete key-value pair by key
print(dict) # prints {'Alex': 24, 'Cathy': 27, 'Bob': 30}

print(len(dict)) # get number of key-value pairs; prints 3

print(dict.keys())  # get all keys; prints dict_keys(['Alex', 'Cathy', 'Bob'])
print(dict.values())  # get all values; prints dict_values([24, 27, 30])

print(dict) # print the entire dictionary; prints {'Alex': 24, 'Cathy': 27, 'Bob': 30}
print(dict.items())  # get all key-value pairs; prints dict_items([('Alex', 24), ('Cathy', 27), ('Bob', 30)])

dict.pop("Cathy") # remove key-value pair by key and return the value
print(dict) # prints {'Alex': 24, 'Bob': 30}

dict.clear()  # remove all key-value pairs
print(dict) # prints {}

# --- This is a horizontal line for separation ---

# date and time module
import time

t = time.time()  # get the current time in seconds since the 1970-01-01 00:00:00 UTC
print(t) # e.g., 1761664812.1211321

local_time = time.localtime() # convert seconds to local time tuple
print(local_time) # e.g., time.struct_time(tm_year=2025, tm_mon=10, tm_mday=28, tm_hour=16, tm_min=22, tm_sec=0, tm_wday=1, tm_yday=301, tm_isdst=0)

str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) # format time tuple to string
print(str_time) # e.g., '2025-10-28 16:23:56'

str_time_2 = time.strftime("%A, %d. %B %Y", time.localtime()) # format time tuple to string with different format
print(str_time_2) # e.g., 'Tuesday, 28. October 2025'

time_stamp = time.mktime(time.strptime(str_time, "%Y-%m-%d %H:%M:%S")) # convert string back to time tuple and then to seconds
print(time_stamp) # e.g., 1761665309.0

# calender module
import calendar

cal = calendar.month(2025, 10) # get the calendar for October 2025
print(cal)
#     October 2025
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30 31
