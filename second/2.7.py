#7 两个正整数的最大公约数
def fun(a, b):
    x = a % b  #ab取余数
    while(x != 0):
        a = b
        b = x
        x = a % b
    return b
a = int(input())
b = int(input())
print(fun(a, b))
