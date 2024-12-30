from collections import defaultdict
import math

def percent(name, name_1):
    combine = name + name_1

    d = defaultdict(int)

    for i in combine:
        if i.isalpha():
            d[i.lower()] += 1

    lst_of_lsts = []

    lst = list(d.values())
    lst_of_lsts.append(lst.copy())
    
    l = []
    
    n = len(lst)
    k = len(lst)

    while k > 2:
        k = math.ceil(k / 2)
        l.append(k)

    for _ in range(len(l)):
        for i in range(0, math.ceil(n / 2)):
            if i != n - i - 1:
                j = lst[i] + lst[n - i - 1]
                lst.append(j % 10)
            else:
                lst.append(lst[i])
        for i in range(0, len(lst) - math.ceil(n / 2)):
            lst.pop(0)
        lst_of_lsts.append(lst.copy())
        n = len(lst)

    return d, lst_of_lsts, lst[0] * 10 + lst[1]

