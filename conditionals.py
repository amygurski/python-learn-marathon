"""
In this section we will look at the first core principal of logic flow branching.
If statemetns are at the core of programming logic. This is the primary mechanism to codify our logic.
An if statement evaluates a boolean expression and responds accordingly based on resulting value.
"""

# basic if True statement
test = 1
if test == 1:
        print("Test is one")
else: 
        print("How was that?")

# If with conditional. - change value of the conditional and try again

"""
This is an important point to discuss python scope. If statement would be the first instance where
we run into the need to use scope. Scope in Python is delineated with indent.
"""

#if statement with several lines of code. Try to execute it with conditional True and False

#if, else. - create conditional followed by some code. Observe that it is executed every time
# create else block and put followup code into "else" block scope.

#if, elif , else - rock, paper, scissors
import random
user = random.choices(["Rock", "Paper", "Scissors"])[0]
pc = random.choices(["Rock", "Paper", "Scissors"])[0]

print (f"User: {user} ; PC: {pc}")

if user == pc:
    print("It's a draw")
else:
    if(user == "Rock" and pc == "Paper") or (user == "Paper" and pc == "Scissors") or (user=="Scissors" and pc == "Rock"):
        print("You lose")
    else:
        print("You win!")
# turnary operator
# value = other_value if other_value else "test"

# value = other_value or "default value" - evaluate if other_value is None

"""
Comprehansion of boolean logic is essential creating correct if statements. Let's review in boolean_logic.py
"""