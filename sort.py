def insertion_sort(input):
    for i in range(1, len(input)):
        key = input[i]
        for j in reversed(range(0, i)):
            if key < input[j]:
                input[j + 1], input[j] = input[j], key
    return input

def merge_sort(input):
    


a = [5, 2, 7, 9, 1, 3]
print(insertion_sort(a))


