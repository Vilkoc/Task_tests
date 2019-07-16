def task11():
    items = []
    num = [x for x in input('Write bin-numbers: ').split(',')]
    for p in num:
        x = int(p, 2)
        if not x % 5:
            items.append(p)
    print(','.join(items))
    return items


if __name__ == '__main__':

     task11()

