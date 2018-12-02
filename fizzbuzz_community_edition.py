from __future__ import print_function

i = 1
# A simple while loop
while i <= 100:
    # % denotes remainder. So, if the remainder of 3 is 0 it'll print Fizz
    if i%3==0:
	# end='something', ends the print function output with something
        print("Fizz", end='')
        if i%5==0:
            print("_Buzz", end='')
    # Else if statement
    elif i%5==0:
        print("Buzz", end='')
    else:
        print(i, end='')
    print()
    i = i + 1
