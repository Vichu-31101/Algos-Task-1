#!/bin/python3
import sys

if __name__ == '__main__':
    arr = [7, 8, 9, 10, 16, 43]
    print("0 1")
    sys.stdout.flush()
    p = int(input())
    for i in arr:
        if p % i == 0 and p // i in arr:
            a = i
            b = p // i
            break

    print("0 2")
    sys.stdout.flush()
    p = int(input())

    for i in arr:
        # To figure out the numbers in the product
        if p % i == 0 and p // i in arr:
            # Adding the first 3 numbers in the reverse order at the end of the list
            if i == a or i == b:
                c = p // i
                if i == b:
                    b = a
                    a = i
                arr.remove(a)
                arr.remove(b)
                arr.remove(c)
                arr.extend([c, b, a])
            else:
                c = i
                if p//i == b:
                    b = a
                    a = p//i
                arr.remove(a)
                arr.remove(b)
                arr.remove(c)
                arr.extend([c, b, a])
            break

    for i in range(2):
        print("0", i + 3)
        sys.stdout.flush()
        p = int(input())
        # Removing and inserting subsequent numbers in the reverse order
        arr.remove(p // a)
        arr.insert(2 - i, p // a)

    # Array reversed to get the correct sequence
    arr.reverse()
    print(arr)
    sys.stdout.flush()
