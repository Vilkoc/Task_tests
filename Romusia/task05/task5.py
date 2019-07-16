class qwerty():
    def __init__(self, tmp):
        self.str1 = tmp

    def get_String(self):

        #self.str1 = input('Write word: ')
        self.str1 = 'qwertyu'
    def print_String(self):

        print(self.str1.upper())
        return (self.str1.upper())


if __name__ == '__main__':
    str1 = qwerty(input('Write word: '))
    #str1.get_String()
    str1.print_String()
