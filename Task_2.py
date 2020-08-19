#!/bin/python3


if __name__ == '__main__':
    size = int(input())
    inp = input()
    div = True
    counter = 0
    if size % 2 == 0:
        while div:
            fInp = inp[0:size//2]
            lInp = inp[size//2:]
            # Condition checking
            if fInp == lInp:
                counter += 1
                inp = fInp
                size //= 2
            else:
                div = False
    print(counter)




