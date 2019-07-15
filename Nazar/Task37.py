def func():
    a = [x ** 2 for x in range(1, 21)]
    return a[5:]


print(func())
