def task41():
  tmp = input('Write "yes": ')

  if tmp == 'Yes' or tmp == 'YES' or tmp == 'yes':
    print("Yes")
    return 'Yes'
  else:
    print("No")
    return "No"


if __name__ == '__main__':
    task41()