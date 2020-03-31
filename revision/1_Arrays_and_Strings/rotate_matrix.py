def rotate_matrix(m):
    l = len(m)
    for i in range(l // 2):
        first, last = i, l - i - 1
        for j in range(first, last):
            temp = m[i][j]
            m[i][j] = m[-j - 1][i]
            m[-j - 1][i] = m[-i - 1][-j - 1]
            m[-i - 1][-j - 1] = m[j][-i - 1]
            m[j][-i - 1] = temp
    return m


m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_matrix(m))
