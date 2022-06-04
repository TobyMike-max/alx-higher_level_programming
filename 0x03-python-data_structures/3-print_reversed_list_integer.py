#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints all integers opf a list in reverse order."""
    count = len(my_list) - 1
    for i in range(count, -1, -1):
        print("{:d}".format(my_list[i]))

print_reversed_list_integer([43, 3, 354, 43653, 324234, 32, 5, 56, 32423])
