#!/usr/bin/python3
for a in range(0, 10):
    for b in range(a + 1, 10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
            #print(f"{a:d}{b:d}")
        else:
            print("{}{}".format(a, b), end=", ")
            #print(f"{a:d}{b:d}", end=', ')
