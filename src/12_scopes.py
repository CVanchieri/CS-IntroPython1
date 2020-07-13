# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
x = 12 # outer variable.
def change_x(): # function.
    x = 99 # inner variable.
change_x() # call function.
print(x) # prints outter variable.
# This prints 12. What do we have to modify in change_x() to get it to print 99?
def change_x(): # create function.
    x = 99 # inner variable.
    print(x) # print inner variable.
change_x() # call function.
print(x) # prints inner variable.

# This nested function has a similar problem.
def outer(): # function.
    y = 120 # outer variable.
    def inner():
        y = 999 # inner variable.
    inner() # call function.
    print(y) # prints outer variable.
    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".   
def outer(): # outer function.
    y = 120 # outer variable.
    def inner(): # inner function.
        y = 999 # inner variable.
        print(y) # prints inner variable.
    inner() # call function.
outer() # call function.
