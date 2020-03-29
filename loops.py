"""
Another very essential part of logic flow is ability to loop. Looping is used in a variety of scenarios:
 - progress over a collection of items
 - repeatedly perform an action until condition is met
 - perform action a set ammount of time
 - create a forever loop that will keep a given program alive, breaking for sleep event, user input, os input
"""

# while loop
# import random
# test = 0
# while test != 10:
#         test=random.randint(0,20)
#         print(f"Test is {test}")

# for loop
days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

# loop over items in a collection
for day in days:
    print(f"This day is {day}")

# loop over items in a dictionary
sample_dict = {"one": "first", "two": 2, "three": True, "four": 4.321}
#this does keys
for k in sample_dict:
    print(f"We got {k}")
    print(f"k type is {type(k)}")
# do keys and values
for k, v in sample_dict.items():
    print(f"We got k: {k} v: {v}")
    print(f"k type is {type(k)}; v type is {type(v)}")
# loop over range - range is a generator

"""
Python has a very powerful optimized ability to iterate over lists of items and manipulate the output if needed.
It's called comptrehansion
"""

#list comprehansion
# convert all the strings with numbers into list of ints

#dictionarry comprehansion
# convert dictionarry with nuber strings for values to integers for values

# zip generator
# take input list that has keys and values interleaving, use zip and list accessors to convert it to normal dict

"""
In process of comprehansion it is possible to not only format output, but also filter out the output that is not needed.
"""

# create a list of values divisible by 3 from range