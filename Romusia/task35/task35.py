def printvalues():
    var = list()
    for i in range(1, 21):
        var.append(i ** 2)
    print(var)
    return var


if __name__ == '__main__':

    printvalues()