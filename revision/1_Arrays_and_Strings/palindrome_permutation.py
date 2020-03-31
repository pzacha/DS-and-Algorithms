def palindrome_permutation(s: str) -> bool:
    char_dict = {}
    uneven = 0
    for c in s:
        if c != " ":
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
    for k in char_dict:
        if char_dict[k] % 2 == 1:
            uneven += 1
        if uneven > 1:
            return False
    return True


print(palindrome_permutation("abcd c a bed"))
