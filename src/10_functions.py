# Read a number from the keyboard
num = input("Enter a number: ") # take an unput from the user.
num = int(num) # set input as int.
# Write a function is_even that will return true if the passed-in number is even.
def print_num(num): # function 
    if num % 2 == 0: # if remainder is 0 its true.
        print("true!")
    else:
        print("false!")
    print(num)
print_num(num) # print result.

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)
# Print out "Even!" if the number is even. Otherwise print "Odd"
def print_num(num):
    if num % 2 == 0:
        print("Even!")
    else:
        print("Odd!")
    print(num)
print_num(num)

