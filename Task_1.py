#!/bin/python3


if __name__ == '__main__':
    exist = True
    size = int(input())
    binary = input()
    bInt = list(map(int, list(binary)))
    bNext = bInt.copy()
    bNext[size - 1] += 1
    bPrev = bInt.copy()
    bPrev[size - 1] -= 1
    for i in reversed(range(size)):
        # To find the next binary
        if int(bNext[i]) == 2 and i != 0:
            bNext[i] = 0
            bNext[i - 1] += 1
        elif int(bNext[i]) == 2 and i == 0:
            # To check if the binary is longer
            exist = False
        # To find previous binary
        if int(bPrev[i]) == -1 and i != 0:
            bPrev[i] = 1
            bPrev[i - 1] -= 1
        elif int(bPrev[i]) == -1 and i == 0:
            # To check if the binary is shorter
            exist = False

    strP = ''.join((str(i) for i in bPrev))
    strN = ''.join((str(i) for i in bNext))
    if exist:
        print(strP, strN)
    else:
        print(-1)
