print("Intro-Python-1")

### hello world ###
print("0. ### hello world ###")
# print hello world
print("Print hello world")
print("hello world")

#### big numbers ###
print("1. ### big numbers ###")
# print out 2 to the 65536 power
print("Print out 2 to the 65536 power")
num1 = 2**65536
num2 = pow(2, 65536)
print("2**65536")
print(num1)
print("pow(2,65536)")
print(num2)

### data types ###
print("2. ### data types ###")
# write a print statement that combines x + y into the integer value 12
print("write a print statement that combines x + y into the integer value 12")
x = 5
y = "7"
val1 = x + int(y)
val2 = str(5) + y
print("x + int(y)")
print(val1)
print("str(5) + y")
print(val2)

### modules ###
print("3. ### modules ###")
print("### sys module ###")
import sys
# print out the command line arguments in sys.argv, one per line
print("print out the command line arguments in sys.argv, one per line")
print(sys.argv[0])
# print out the OS platform you're using
print("print out the OS platform you're using")
print(sys.platform)
# print out the version of Python you're using
print("print out the version of Python you're using")
print(sys.version)
### os module ###
print("### os module ###")
import os
# print the current process ID
print("print the current process ID")
print(os.getpid())
# print the current working directory (cwd)
print("print the current working directory (cwd)")
print(os.getcwd())
# print out your machine's login name
print("print out your machine's login name")
print(os.getlogin())

### print statements ###
print("4. ### print statements ###")
# using the printf operator (%), print the following feeding in the values of x, y, and z:
print("x is 10, y is 2.25, z is I like turtles!, with format string")
x = 10
y = 2.24552
z = "I like turtles!"
print('x is {}, y is {}, z is {}'.format(x, y, z))
#Use the 'format' string method to print the same thing
print("print the same thing using an f-string, with f string")
print(f"x is {x}, y is {y}, z is {z}")

### lists ###
print("5. ### python lists ###")
x = [1, 2, 3]
y = [8, 9, 10]
print(f"x = {x}")
print(f"y = {y}")
# change x so that it is [1, 2, 3, 4]
print("change x so that it is [1, 2, 3, 4]")
x.append(4)
print("x.append(4)")
print(f"x is now = {x}")
# using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
print("using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]")
x.extend(y)
print("x.append([y])")
print(f"x is now = {x}")
# change x so that it is [1, 2, 3, 4, 9, 10]
print("change x so that it is [1, 2, 3, 4, 9, 10]")
x.remove(8)
print("x.remove(8)")
print(f"x is now = {x}")
# change x so that it is [1, 2, 3, 4, 9, 99, 10]
print("change x so that it is [1, 2, 3, 4, 9, 99, 10]")
x.insert(5, 99)
print("x.insert(5, 99)")
print(f"x is now = {x}")
# print the length of the list
print("print the length of the list")
length = len(x)
print("length(x)")
print(f"list x length is = {length}")
# print all the values in x multiplied by 1000
print("Print all the values in x multiplied by 1000")
x2 = []
for i in x:
    x2.append(i * 1000)
print("""x2 = []
for i in x:
    x2.append(i * 1000)""")
print(x2)





### notes from class ###
print("### notes from class ###")

# lists
lst1 = [1, 4, 10, 50, 23]
# full list
print(lst1)
# 2nd object in the list
print(lst1[2])
lst2 = [1, 4, "cat", 50, 23]
# full list
print(lst2)
# 2nd object in the list
print(lst2[2])
# adding object to a list
lst3 = [1, 4, "cat", 50, 23]
lst3.append(3.5)
# full list
print(lst3)
# 2nd object in the list
print(lst3[5])
lst3.append("dog")
# full list
print(lst3)
# 2nd object in the list
print(lst3[6])
lst3.append([100, 200, 300])
# full list
print(lst3)
# 2nd object in the list
print(lst3[7])
# inserting object to a specfic place
lst3.insert(2, "hello")
# full list
print(lst3)
# 2nd object in the list
print(lst3[2])

# loops
for elm in lst3:
    print(elm)
for i in range(6):
    print(i)
    print(lst3[i])

# dictionaries
dic={"foo":12, "bar": 34}
print(dic)
val = dic["foo"]
print(val)

# f string
print(f' garbage {val}')
num = 1010.256
print(f"value {num}")
