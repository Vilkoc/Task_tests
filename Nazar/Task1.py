def numbers():
    x = ''
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            x += str(i) + ", "
    return x[:-2]


print(numbers())