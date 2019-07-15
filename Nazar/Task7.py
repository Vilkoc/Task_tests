def lst(x, y):
    ls = [[0 for y in range(y)] for x in range(x)]
    for i in range(x):
        for j in range(y):
            ls[i][j] = i * j
    return ls


r = int(input("rows: "))
c = int(input("columns: "))

print(lst(r, c))
