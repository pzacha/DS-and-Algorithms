import unittest


def len_diff(bigger, smaller):
    i1 = 0
    i2 = 0
    while i1 < len(bigger) and i2 < len(smaller):
        if bigger[i1] != smaller[i2]:
            if i1 != i2:
                return False
            else:
                i1 += 1
        else:
            i1 += 1
            i2 += 1

    return True


def one_away(s1: str, s2: str) -> bool:
    l1 = len(s1)
    l2 = len(s2)
    dif = 0
    if abs(l1 - l2) > 1:
        return False
    if l1 == l2:
        for i in range(l1):
            if s1[i] != s2[i]:
                dif += 1
            if dif > 1:
                return False
        return True
    else:
        if l1 > l2:
            return len_diff(s1, s2)
        else:
            return len_diff(s2, s1)


print(one_away("pale", "ple"))
print(one_away("pale", "pales"))
print(one_away("pale", "bale"))
print(one_away("pale", "bae"))
