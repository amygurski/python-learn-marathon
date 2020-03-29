# Let's cover collections and all the wonderful things we can do with them
# While pandas and numpy do wonders and havevery potent c based parallelized code underneath them
# Python's native collections are quite magnificent and performance optimized themselves.
# We will play with basics of the underlying language and see the power of what we can do right here

## TUPLE
# declare - empty full
first_one = tuple()
print('Empty tuple is just tuple(): ', type(first_one))
one_element = (123, )
print('One element is just (123, ) :', one_element, type(one_element))
multi_type_tup = (123, False, 123.45)
print(multi_type_tup, type(multi_type_tup))

print('Assign each one to variable then access individually: ')
this_int, is_it_true, my_string = multi_type_tup
print(this_int)
print(is_it_true)
print(my_string)

# access elements
print('--------------')
print('Index-based access: ', multi_type_tup[1])
# try changing values
multi_type_tup = (123, False, 'Yay')
print(multi_type_tup)


## LIST
# declare - empty, full
empty_list = []
a_list = [1,2,3,4,5]
# create using '*' operator
small_list = [0]*20
print(small_list)
small_list = (1,2,3) * 10
print(small_list)
matrix = [[1,2,3,4,5]] * 5
print(matrix)

# access
print(small_list[5])
# mutate
alter_me = [2,3,4,5,6]
alter_me[3] = "Testing"

# pile on different types
alter_me[4] = True

# splice - get some from the end, some from the begining, everyother one, etc.
print("="*20 + "Splicing" + "="*20)

big_list = [i for i in range(100)]
print(big_list)
print(big_list[-1])

# start 5 elements in from end and grab the rest
print(big_list[-5:])
# add lists, append item to list

# randomly select a value out of a list - options
import random
rnd_val = random.choices(["Mon", "Tues", "Wed"])
print(rnd_val)

# shuffle contents of the list - shuffle
random.shuffle(big_list)
print(big_list)
print("#"*20 + " SET " + "#"*20)

## SET
# declare - empty, full
first_set = set()
print(type(first_set))
second_set = {1,2,3,4,5,6,7}
print(second_set, type(second_set))

# feed a list of repeating elements to a set
list_one = [i for i in range(10)]
list_two = [i for i in range(5,15)]
list_all = list_one + list_two
print('Combine two arrays: ', list_all)
print('Use set to not get duplicates: ', set(list_all))

# set math - & | ^
print('List 1: ', list_one)
print('List 2: ', list_two)
print('Sutract List 1 - List 2:', (set(list_one) - set(list_two)))
print('Subtract List 2 - List 1: ', (set(list_two) - set(list_one)))

print('Use | to combine: ', set(list_one) | set(list_two))
print('Use & for intersection (inner join): ', set(list_one) & set(list_two))
print('Use ^ for non-intersection (outer join): ', set(list_one) ^ set(list_two))

#access
set_one = set(list_one)
one_val = set_one.pop()
set_one.add(5)
set_one.add(-1)
print(one_val)
print('Popped one off front an added a -1: ', set_one)

## DICTIONARY
# declare - empty, full
first_dict = {}

second_dict = {'first': 123.0, "second": True, "third": "Some string here"}
print('Dictionary: ', second_dict)

third_dict = {123.4: "test", "something else": 456}
print('Another Dictionary: ', third_dict)

crazy_dict = {(123, "2020-02-23"): "Some value here", (1234, "2020-03-23"): "Something else"}
print('Crazy dictionary: ', crazy_dict)

nice_dict = {'weight': 130, 'height': 62, "first_name": "Amy", "last_name": "Gurski"}
print('Nice dictionary: ', nice_dict)

# bad_dict = {[1, 'a']: "value"}
# print(bad_dict) 
# unhashable type: 'list'

# key, value - is it hashable (try declaring with list)
print("Hashing a string 'Let's see what this does'", hash("Lets see what this does"))

print('Height from nice dict: ', nice_dict["height"])

# add
print(nice_dict)
nice_dict['middle-name'] = 'Zippady'
print('Added middle name: ', nice_dict)
nice_dict['temp-reads'] = [30,33,43]
print('Adding a list as values: ', nice_dict)

# join lists - update
nice_dict.update(crazy_dict)
print(nice_dict)

# we will cover comprehension once we go over loops