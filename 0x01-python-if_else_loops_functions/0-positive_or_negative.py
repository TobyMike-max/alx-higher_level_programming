#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
    #print(f"{number:d} is positive")
elif number == 0:
    print("{} is zero".format(number))
    #print(f"{number:d} is zero")
else:
    print("{} is negative".format(number))
    #print(f"{number:d} is negative")