def insertion_sort(input):
    for i in range(1, len(input)):
        key = input[i]
        for j in reversed(range(0, i)):
            if key < input[j]:
                input[j + 1], input[j] = input[j], key
    return input


def merge_sort(input):
    # input length
    l = len(input)
    # input middle index
    m = int(l / 2)
    # output list
    merged = []
    if l > 1:
        s1 = merge_sort(input[:m])
        s2 = merge_sort(input[m:])
        for i in range(l):
            if len(s1) == 0:
                merged.append(s2.pop(0))
            elif len(s2) == 0:
                merged.append(s1.pop(0))
            else:
                if s1[0] < s2[0]:
                    merged.append(s1.pop(0))
                else:
                    merged.append(s2.pop(0))
        return merged
    else:
        return input


a = [5, 2, 7, 9, 1, 3]
print(insertion_sort(a))
print(merge_sort(a))
