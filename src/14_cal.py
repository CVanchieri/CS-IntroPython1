"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""
import sys
import calendar
from datetime import datetime
# if the user doesnt specify any input, your program should print the calendar for the current month.
if len(sys.argv) == 1: # if statement for no user input, sys takes in command line input.
    print(calendar.month(datetime.now().year, datetime.now().month))
# if user inputs a month argument, print calendar of that month and the current.
elif len(sys.argv) == 2: # if statement for 1 user input for month, sys takes in command line input.
        print(calendar.month(datetime.now().year, int(sys.argv[1])))
# if the user specifies two arguments, assume they passed in both the month and the year. Render the calendar for that month and year.
elif len(sys.argv) == 3:# if statement for 2 user input for year and month, sys takes in command line input.
        print(calendar.month(int(sys.argv[2]), int(sys.argv[1])))
# otherwise, print a usage statement to the terminal indicating the format that your program expects arguments to be given. Then exit the program.
else:
    print("expected input format is 14_cal.py [month] [year]") # print statement displaying proper input entry.
    sys.exit() # exit sys.
