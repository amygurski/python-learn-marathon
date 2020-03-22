"""
In this module we are going to be covering strings, string formatting and string manipulation.
This comment is a multiline string.
"""

# Single line string literal
first_string = "This is a simple string."
second_string = 'This is another string'
first_string = "This isn't important"
second_string = 'This contains "double" options'
third_string = "Double quotes can be escaped \" like this"
print(third_string)
fourth_string = "We have new lines here\nCheck us out"
print(fourth_string)

# Multiline string literal
multiline = """
This is a multiline string.
See it keeps going
La di da
"""
print(multiline)

# f-string and f-string formatting
number_of_ways = 4
print("f-string formatting. This is {} way.. But there are {} others. Like {}".format("one", "few", number_of_ways))
first_name = "this"
last_name = "person"
age = 20
print(f"We are looking at {first_name} {last_name} of {age} age")
print(f"They are {'young' if age < 30 else 'old'}")
# splitting a string
input = "Let's test this string with a bunch of words"
result = input.split(" ")
print(result[::2])

chat_command = "!alarm this is outragous!!!"
tokens = chat_command.split(" ")
command = tokens[0]
print(command)

# joining a string
phrase = " ".join(tokens[1:]) #threw out index 0, joined the rest
print(phrase)

# stripping leading and trainling spaces
sample_str = "     There are some spaces here before and after          "
print(sample_str.strip())

# case manipulation
print(f"Is command !ALARM {tokens[0].upper() == '!ALARM'}")
print("!HALP".lower())

# let's build a random IP address
# goal eg. "127.234.20.129"
import random
#print(str(random.randint(100,255)) + "." + str(random.randint(100,255)) + "." + str(random.randint(0,99)) + "." + str(random.randint(100,255)))
print(".".join([str(random.randint(0,255)) for _ in range(4)]))
