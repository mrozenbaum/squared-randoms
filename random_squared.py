# Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.
import random

random_numbers = [random.randint(0,49) for x in range(0,20)]
print(random_numbers)

# With the resulting list, use a list comprehension to build a new list that contains each number squared. 
squared_list = [x ** 2 for x in random_numbers]
print(squared_list)
