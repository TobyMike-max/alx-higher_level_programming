#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastD = str(number)[-1]
lastD = int(lastD)
if number < 0:
    lastD = lastD * (-1)
# Test for print output
if lastD > 5:
    print(f"Last digit of {number:d} is {lastD:d} and is greater than 5")
elif lastD == 0:
    print(f"Last digit of {number:d} is {lastD:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lastD:d} and is less than 6 and not 0")
