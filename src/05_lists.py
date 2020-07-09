# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print("change x so that it is [1, 2, 3, 4]")
x.append(4)
print("x.append(4)")
print(f"x is now = {x}")

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print("using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]")
x.extend(y)
print("x.append([y])")
print(f"x is now = {x}")

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print("change x so that it is [1, 2, 3, 4, 9, 10]")
x.remove(8)
print("x.remove(8)")
print(f"x is now = {x}")

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
x.insert(5, 99)
print("x.insert(5, 99)")
print(f"x is now = {x}")

# Print the length of list x
length = len(x)
print("length(x)")
print(f"list x length is = {length}")

# Print all the values in x multiplied by 1000
x2 = []
for i in x:
    x2.append(i * 1000)
print("""x2 = []
for i in x:
    x2.append(i * 1000)""")
print(x2)
