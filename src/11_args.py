# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.
def f1(a, b): # function with 2 arguments.
    return a + b # return sum of arguments.
print(f1(1, 2)) # use function and print.

# Write a function f2 that takes any number of integer arguments and returns the
# sum.
# Note: Google for "python arbitrary arguments" and look for "*args"
def f2(*args): # function with *args that takes any # of arguments.
    sum = 0 # starting sum.
    for i in args: # for loop to add each variable together
        sum += i # add the variable to the sum.
    return sum # return the total

print(f2(1))                    # Should print 1
print(f2(1, 3))                 # Should print 4
print(f2(1, 4, -12))            # Should print -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33

a = [7, 6, 5, 4] # list.

# How do you have to modify the f2 call below to make this work?
print(f2(*a)) # with *, takes in each variable from the list.   # Should print 22 

# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments.
# Note: Google "python default arguments" for a hint.
def f3(a, b=1): # function where b=1 unless a new variable is used.
    return a + b # return the sum of the variables.
print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
#
# key: foo, value: bar
# key: baz, value: 12
#
# Note: Google "python keyword arguments".
def f4(**kwargs): # function with **kwargs for key words.
    for k, v in kwargs.items(): # for loop to print keys and values.
        print("key: {k}, value: {v}".format(k=k, v=v)) # print key and values with format.
# Should print
# key: a, value: 12
# key: b, value: 30
f4(a=12, b=30) # call function on variables.

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
f4(city="Berkeley", population=121240, founded="March 23, 1868")
d = {
    "monster": "goblin",
    "hp": 3
}
# How do you have to modify the f4 call below to make this work?
f4(**d) # ** allows use to write new keys.
