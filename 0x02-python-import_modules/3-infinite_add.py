#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    total = 0
    count = len(argv)

    if count == 1:
        print(0)
    else:
        for i in range(1, count + 1):
            total = total + int(argv[i])
        print("{}".format(total))

