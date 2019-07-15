from operator import itemgetter


def sort(x):
    return sorted(x, key=itemgetter(0, 1, 2))


a = [('Json', '19', '85'), ('John', '20', '90'), ('Jony', '17', '95'), ('Jony', '17', '93'), ('Json', '21', '85')]

print(sort(a))
