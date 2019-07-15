def numbers(n):
    x = ''
    for i in range(0, n):
        if i % 7 == 0 and i % 5 == 0:
            x += str(i) + ", "

    return x[:-2]


a = int(input("Input n: "))
print(numbers(a))



