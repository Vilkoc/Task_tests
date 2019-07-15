import re


def num(b):
    d = re.sub("[^0-9]", " ", b).split()
    return d


a = input("Input text: ")

print(num(a))
