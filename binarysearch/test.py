def hello(num):
    num = str(num)
    print(num[0])
    if len(num) == 1:
        return num
    return hello(num[1:])


num = 1234
hello(num)
