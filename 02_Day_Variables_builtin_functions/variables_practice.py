# Lab 2: Variables and Built-in Functions

# ===========================================================================
# Problem 1: Create Your Variables
# ===========================================================================

"""
Task
----
Create variables for:

1. First name
2. Last name
3. Full name
4. Country
5. City
6. Age
7. Birthyear
8. Is married
9. Is true
10. Is light on

Example format
--------------
# Day 2: 30 Days of python programming
first_name = "Asabeneh"
last_name = "Yetayeh"
country = "Finland"
city = "Helsinki"
age = 250
birthyear = 1771
is_light_on = True

TODO
----
Write your code under this comment.
"""
# Day 2: 30 Days of python programming
first_name = 'Sanjid'
last_name = 'Shopnil'
full_name = 'Sanjid Arefin Shopnil'
country = 'Bangladesh'
city = 'Dhaka'
age = 26
birthyear = 1999
is_married = False
is_true = True
is_light_on = True


# ===========================================================================
# Problem 2: Multiple Variables in One Line
# ===========================================================================

"""
Task
----
Declare multiple variables in one line.

Example format
--------------
first_name, last_name, country, age = "Asabeneh", "Yetayeh", "Finland", 250

TODO
----
Write your code under this comment.
"""

first_name, last_name, country, age = "Sanjid", "Shopnil", "Bangladesh", 26

# ===========================================================================
# Problem 3: Print Your Variables
# ===========================================================================

"""
Task
----
Print the variables you created in Problem 1.

Example format
--------------
print("First name:", first_name)
print("Age:", age)
print("Birthyear:", birthyear)

TODO
----
Write your code under this comment.
"""
print('First name:',first_name)
print('Last name:',last_name)
print('Full name:',full_name)
print('Country:',country)
print('City:',city)
print('Age:',age)
print('Marrige status:',is_married)
print('Light status:',is_light_on)



 
 
 




# ===========================================================================
# Problem 4: Check Data Types
# ===========================================================================

"""
Task
----
Use type() to check the data type of your variables.

Example format
--------------
print(type(first_name))
print(type(age))
print(type(birthyear))
print(type(is_light_on))

TODO
----
Write your code under this comment.
"""
print(type(first_name))
print(type(age))
print(type(birthyear))
print(type(is_light_on))


# ===========================================================================
# Problem 5: Use len()
# ===========================================================================

"""
Task
----
Use len() to:

1. Find the length of your first name
2. Find the length of your last name
3. Compare which name is longer

Example format
--------------
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))

TODO
----
Write your code under this comment.
"""
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))


# ===========================================================================
# Problem 6: Basic Math with Variables
# ===========================================================================

"""
Task
----
Declare:

num_one = 5
num_two = 4

Then calculate and print:

1. total
2. diff
3. product
4. division
5. remainder
6. exp
7. floor_division

Example format
--------------
total = num_one + num_two
print("Total:", total)

TODO
----
Write your code under this comment.
"""
total = 5+4
diff = 5-4
product = 5*4
division = 5/4
remainder = 5%4
exp = 5**4
floor_division = 5//4


# ===========================================================================
# Problem 7: Circle Area and Circumference
# ===========================================================================

"""
Task
----
The radius of a circle is 30 meters.

Use:
pi = 3.14

Calculate and print:

1. area_of_circle
2. circum_of_circle

Formulas
--------
area = pi * radius * radius
circumference = 2 * pi * radius

TODO
----
Write your code under this comment.
"""
radius = 30
pi = 3.1416
area = pi * radius * radius
circumference = 2 * pi * radius
print(f'area is {area} meter and circumference is {circumference} meter')
# ===========================================================================
# Problem 8: User Input
# ===========================================================================

"""
Task
----
Use input() to get:

1. First name
2. Last name
3. Country
4. Age

Then print the values.

Example format
--------------
user_first_name = input("What is your first name? ")
print(user_first_name)

TODO
----
Write your code under this comment.
"""
name = input('Enter your name: ')
password = input ('enter your password: ')
integer_password = int(password)

# ===========================================================================
# Problem 9: Python Keywords
# ===========================================================================

"""
Task
----
Run help("keywords") to see Python reserved words.

TODO
----
Uncomment the line below when you want to see the keywords.
"""

help("keywords")
