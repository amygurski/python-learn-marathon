"""
There is a variety of ways to evaluate truthiness of something.
"""

# basic truthiness of values
# int
val = 20
if val:
        print("val is true")

# float
print(f"Value 0.0 is float: {bool(0.0)}")
print(f"Value 0.1 is float: {bool(0.1)}")

# collection
print(f"List with one element is {bool(['Test'])}")


# None
val = None
print(f"A variable with value None is {bool(val)}")
print(f"Is val equal to None: {val is None}")

# string
print(f"String with 1 char is {bool('0')}")


# comparison - < > == != <= >=
val = 5
print(f"is val {val} between 3 and 7 {val >=3 and val <=7}")
print(f"is val {val} outside of [4..6] {val < 4 or val > 6}")
print(f"is 5 == 5.0 {5==5.0}")
print(f"is 5 != 5 {5 !=5}")


# in operator
# value in collection
characters = ['a', 'b', 'c']
print(f"is z in the list {'z' in characters}")

#substring in string
print(f"is 'lo' in hello, world {'lo' in 'Hello, World'}")

# key in dictionary
person = {"fname": "Amy", "age": 34}
print(f"does {person['fname']} have age over 30 {person['age'] > 30}")
