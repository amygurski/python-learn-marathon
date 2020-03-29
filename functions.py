"""
One of very powerful common constructs in modern languages is function.
It gives you an ability to logically group the code, redistribute and reuse it.
"""

# let's build a greeting function
# 1) print Greetings to you from Python
# 2) pull "Python" out into a variable
# 3) wrap both lines into a function without a parameter - discuss scope
# 4) run code and see that function is not executed
# 5) call declared function
# 6) turn variable with value "Python" into parameter and pass literal to the function
# 7) use formatting from within print to create a greeting and return it, print returned value outside
def greetings_from(name):
        formatted_str = f"Greetings to you from {name}"
        return formatted_str

donkey_lobster = "python"
result = greetings_from(donkey_lobster)
print(result)
#revisit scope

# passing positional parameters in
def display_pos_params(first, second, third):
    print(f"{first} {second} {third}")

display_pos_params(9, "test", 2)

# passing in key word arguments
def display_kwargs(one, two, k_one=1, k_two="two", k_three=None, k_four="some val"):
    print(f"{one} {two} {k_one} {k_two} {k_three} {k_four}")

display_kwargs("first", 2)
display_kwargs(1, "second", k_three="other than none")

# default values

# beware of mutable default values
print("-- Crazy stuff --")
def crazy_stuff(dont_mutate_me=[]):
    for i in range(5):
        dont_mutate_me.append(i)
    return dont_mutate_me

print(crazy_stuff(dont_mutate_me=[1,2]))
print(crazy_stuff())
print(crazy_stuff())
print(crazy_stuff())

#instead set to None
print("-- Fix for crazy stuff --")
def less_crazy_stuff(dont_mutate_me=None):
    dont_mutate_me = dont_mutate_me or []
    for i in range(5):
        dont_mutate_me.append(i)
    return dont_mutate_me


print(less_crazy_stuff())
print(less_crazy_stuff())
# creating and accessing optional positional parameters and keyword arguments 

# passing kwargs through without reusing them

# unrolling dictionarry into parameters

# returning multiple values and unrolling them into a tuple

# type hints - simple types

# type hints - collection

# yield key word and generators

# switch case using dictionarry and functions (add, sbutract, multiply, divide)

# lambda

# same switch case with lambdas

# closure in lambda - using variable from external scope
