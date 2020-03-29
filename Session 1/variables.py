# let's cover literals and variables
"""
Python is a strong dynamic typed language, meaning it keeps true with assigned types,
does type checking and does not perform type coersion.
"""
# declare an int
i = 234
print('Int: ', i, type(i))

# declare a float
f = 123.456
print('Float: ', f, type(f))

remainder = 2134 % 24
print('Float from remainder of two ints: ', remainder, type(remainder))

float_div= 2134/24
print('Float from integer division: ', float_div, type(float_div))

print("---------------------------------------")

# declare a boolean
is_it_true = True
is_it_false = False
print('Boolean True: ', is_it_true, type(is_it_true))

# declare a string
this_is_me = "This is a nice string with stuff"
print('String: ', this_is_me, type(this_is_me))
#can be single or double quotes

#create a type error
#Type error: can only concatenate str (not int) to str
# print(this_is_me + i)
#instead cast i to string:
print('String concat: ', this_is_me + str(i))

# no type error for int and float
print('Adding int and float: ', i+f, type(i+f))

#float to int
print('float cast to int: ', f, ' becomes ', int(f))
print('float cast to int: ', 123.999, ' becomes ', int(123.999))