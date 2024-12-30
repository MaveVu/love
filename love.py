from collections import defaultdict
import math

def percent(name, name_1):
    combine = name + name_1

    d = defaultdict(int)

    for i in combine:
        if i.isalpha():
            d[i.lower()] += 1

    lst = list(d.values())
    l = []
    
    n = len(lst)
    k = len(lst)

    while k > 2:
        k = math.ceil(k / 2)
        l.append(k)

    # print(list(d.items()))
    # print(list(d.values()))
    print(d)

    for loops in range(len(l)):
        for i in range(0, math.ceil(n / 2)):
            if i != n - i - 1:
                j = lst[i] + lst[n - i - 1]
                lst.append(j % 10)
            else:
                lst.append(lst[i])
        for i in range(0, len(lst) - math.ceil(n / 2)):
            lst.pop(0)
        print(lst)
        n = len(lst)

    return lst[0] * 10 + lst[1]


name = input("Enter your name: ")
name_1 = input("Enter your bf/gf's name: ")
print(f"{name} + {name_1}: {percent(name, name_1)}%")
print(f"{name_1} + {name}: {percent(name_1, name)}%")
