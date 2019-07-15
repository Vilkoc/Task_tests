import re


def lm(x):
    d = re.sub("[^0-9]", "", x)
    let = re.sub("[^a-zA-Z]", "", x)
    return 'Numbers: {}'.format(len(d)), 'Letters: {}'.format(len(let))


a = input("Input text: ")

print(lm(a))
