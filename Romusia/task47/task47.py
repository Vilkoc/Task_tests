import re


def task47():

    emailaddress = input("Enter email addresses: ")

    pat2 = "(\w+)@((\w+\.)+(com))"

    r2 = re.match(pat2, emailaddress)

    print(r2.group(1))
    return r2.group(1)


if __name__ == '__main__':
    task47()