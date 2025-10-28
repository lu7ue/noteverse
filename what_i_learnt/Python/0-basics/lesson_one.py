# 1. Comments
# this is a comment
''' 
this is a multi-line comment
comments can span multiple lines
'''

# 2. Printing to the console
print("Hello, World!")

# 3. Indentation
# note: wrong indentation will have 'IndentationError: unexpected indent' error

# 4. Naming conventions:
# for variables, functions and modules: use_lower_case_with_underscores
# for classes: UseCapitalizedWords
# for constants: USE_ALL_CAPS

# 5. Variables
counter = 100          # An integer assignment
height   = 1.8       # A floating point assignment

name    = "John"       # A string assignment
print(len(name))  # prints the length of the string stored in name

# 6. List - the elements are changeable; use [] to define a list
number_list = [1, 2, 3, 4, 5] # A list of integers
string_list = ["apple", "banana", "cherry"]  # A list of strings
mixed_list = [1, "two", 3.0, True]  # A list with mixed data types

print(number_list[1])  # Accessing the second element of the list

mixed_list[2] = "three"  # Changing the third element of the list
print(mixed_list)  # prints the modified list

# 7. Tuple - the elements are unchangeable; use () to define a tuple
number_tuple = (1, 2, 3, 4, 5)  # A tuple of integers
string_tuple = ("apple", "banana", "cherry")  # A tuple of strings
mixed_tuple = (1, "two", 3.0, True)  # A tuple with mixed data types

# 8. Dictionary - use {} to define a dictionary
map = {"Alice": 24, "Josh": 22, "Mike": 27}  # A dictionary with string keys and integer values
print(map["Alice"])  # Accessing the value with the key

map["Alice"] = 25  # Changing the value associated with the key "Alice"
print(map)  # prints the modified dictionary

# 9. Math operations
a = 1
b = 2
c = a + b
print(c)  # prints 3

d = a * b
print(d)  # prints 2

# 10. Comparison operators
if a > b:
    print("a > b")
else:
    print("a <= b")

# 11. Augmented assignment operators: it has +=, -=, *=, /=, %=, //=, **=
e = 3
f = 2
e = e + f  # e is now 5
print(e)   # prints 4
e += f     # e is now 5
print(e)   # prints 5
e += f     # e is now 7
print(e)   # prints 7

# 12. Logical operators: and, or, not
g = 1
h = 0

if g and h:
    print("Both g and h are true")
else:
    print("Either g or h is false") # prints this line

if g or h:
    print("At least one of g or h is true") # prints this line
else:
    print("Both g and h are false")

if not h:
    print("h is false") # prints this line
else:
    print("h is true")

# 13. Membership operators: in, not in
my_list = [1, 2, 3, 4, 5]

if 3 in my_list:
    print("3 is in the list")  # prints this line
else:
    print("3 is not in the list")

if 6 not in my_list:
    print("6 is not in the list")  # prints this line
else:
    print("6 is in the list")

# 14. If statement: must have at least one 'if', might have max one 'else', and could have multiple 'elif'
j = 3
if j > 2:
    print("j > 2")
elif j == 2:
    print("j == 2")
else:
    print("j < 2")

# 15. Nested if statements
k = 5
if k > 2:
    if k < 10:
        print("2 < k < 10")  # prints this line
    else:
        print("k >= 10")
else:
    print("k <= 2")

# 16. While loop
sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i = i + 1
print(sum)  # prints 55
print(i)  # prints 11

# 17. For loop
sum = 0
for i in range(1, 11):  # from 1 to 10, 1 <= i < 11
    sum = sum + i
print(sum)  # prints 55
print(i)  # prints 10

# 18. Nested loop
k = 0
sum = 0
while k < 3:
    for i in range(1, 6):  # from 1 to 5, 1 <= i < 6
        sum = sum + i
    k = k + 1
print(sum)  # prints 45: loop runs 3 times('k' from 0 to 2), each time 'i' will run from 1 to 5, then 'k' will increase by 1, then repeat to next 'k' until 'k' is not less than 3
print(k)  # prints 3

# 19. Break statement
sum = 0
for i in range(1, 11):
    if i == 6:
        break
    sum = sum + i
print(sum)  # prints 15: when 'i' is 6, the loop will break（stop）

# 20. Continue statement
sum = 0
for i in range(1, 11):
    if i == 6:
        continue
    sum = sum + i
print(sum)  # prints 49(55 - 6): when 'i' is 6, the loop will skip the rest of the code in the loop and go to the next iteration straightaway

# 21. Pass statement: used as a placeholder for future code
a = 1
if a > 0:
    print("a > 0")
else:
    pass  # do nothing