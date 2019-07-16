def task23():
    #number1 = input("First number: ")
    #number2 = input("\nSecond number: ")
    number1 = 5
    number2 = 10

    sum = float(number1) + float(number2)

    print("The sum of {0} and {1} is {2}" .format(number1, number2, sum))
    return sum

if __name__  == '__main__':
    print(task23())