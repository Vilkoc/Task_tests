def task29():
    num = int(input("Enter a number: "))
    mod = num % 2
    if mod > 0:
        print("It is an odd number.")
        return 'odd'
    else:
        print("It is an even number.")
        return 'even'


if __name__ == '__main__':
    task29()