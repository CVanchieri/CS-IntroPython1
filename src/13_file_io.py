"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"
with open('foo.txt', 'r') as f: # open document.
    print("foo.txt contents:", f.read()) # read document.
    f.close() # close.

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain
with open('bar.txt', 'x') as f: # open document.
    f.write("3 lines of text, this is the 1st line. \n This is the 2nd line. \n This is the 3rd line.") # write in the document.
    f.close() # close the document.
with open('bar.txt', 'r') as f:
    print("bar.txt contents:", f.read())
