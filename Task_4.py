#!/bin/python3


if __name__ == '__main__':
    n, r, x, y = input().split()
    c = input().split()
    s = input().split()
    r = 0
    x = int(x)
    y = int(y)
    for i in range(int(n)):
        # Checking if there is a contest on a particular day
        if int(c[i]) == 1:
            if int(s[i]) == 1:
                r += x
            else:
                r -= y
    if r > 0:
        print("promoted")
    elif r < 0:
        print("demoted")
    else:
        print("no change")
