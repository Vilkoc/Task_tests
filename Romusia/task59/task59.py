import random


def task59():
    my_randoms = []
    for i in range(5):
        my_randoms.append(random.randrange(1, 101, 1))
    print(my_randoms)


if __name__ == '__main__':
    task59()