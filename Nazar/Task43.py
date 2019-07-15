def square(n):
    return n ** 2


numbers = [x for x in range(1, 11)]

result = map(square, numbers)

print(result)
