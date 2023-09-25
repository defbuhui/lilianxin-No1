#1 尽可能的多拆分成3 其次是2 不要拆分成1
def fun (n):
    if n<5:
        return n
    #divmod 内置函数 返回商和余数
    a,b = divmod(n,3)
    if b==0:
        return 3**a
    elif b==1:
        return 3**(a-1)*4
    else:
        return 3**a*2
print(fun(int(input("请输入一个数使得拆分以后的积最大"))))
#1)2001 = 3*667 所以拆分成667个3 结果为3**667
#2）通过前面简单数字得到规律 尽可能拆分成3 或2 不要拆分成1 所以优先除以3
#2
print(2**10)
print(2**20)
print(2**30)
print(2**40)
print(2**50)
#增长速度很快 每次大概扩大一千倍
#3 渡河问题 使用循环或者递归算法
def search(step):
    if a[step][0]+a[step][1]+a[step][2]+a[step][3]==4:
        for i in  range(step+1):
            print("east",end = ' ')
            if a[i][0]==0:
                print("wolf",end = ' ')
            if a[i][1] == 0:
                print("goat", end=' ')
            if a[i][2] == 0:
                print("cabbage", end=' ')
            if a[i][3] == 0:
                print("farmer", end=' ')
            print ("none",end = ' ')
            print(end = ' ')
            print("west:",end = ' ')
            if a[i][0]==1:
                print("wolf",end = ' ')
            if a[i][1] == 1:
                print("goat", end=' ')
            if a[i][2] == 1:
                print("cabbage", end=' ')
            if a[i][3] == 1:
                print("farmer", end=' ')
            if not (a[i][0] or a[i][1] or a[i][2] or a[i][3]):
                print('none',end = " ")
            print('\\n')
            if i<step:
                print('the %d time'%(i+1))
            if i>0and i<step:
                if a[i][3]==0:
                    print("----->farmer",end = ' ')
                    print(name[b[i]+1]
                else:
                    print("<----farmer",end = ' ')
                    print(name[b[i] + 1]
                    print('\\n\\n\\n'))
            return
        for i in range(step):
            if a[i]==a[step]:
                return
            if a[step][1]!=a[step][3]and(a[step][2]==a[step][1] or a[step][0]==a[step][1]):
                return
        for i in range (-1,3):
            b[step] = i
            a[step+1] = a[step][:]
            a[step+1][3] = 1-a[step+1][3]
            if i==-1:
                search(step+1)
            elif a[step][i]==a[step][3]:
                a[step+1][i]==a[step+1][3]
            search(step+1)
if __name__=="__main__":
    N=15
    a[[0]*4for i in range]
    b = [0]*N
    name = [" ","and wolf","and goat","and cabbage"]
    print("农夫过桥问题")
    search(0)
#4 while循环实现求解根号2 二分查找
def search (x,epsilon):
    low = 0.0
    high = max(1.0,x)
    average = (low+high)/2.0
    while abs(average**2 - x) >= epsilon:
        if average**2<x:
            low = average
        else:
            high = average
        average = (high+low)/2.0
    return average
print (search(2,0.0000001))
#4笨方法while
def square_root ():
     c = 2
     i = 0
     g = 0
     for j in range(0,c+1):
         if (j*j>c and g==0):
             g = j-1
    while(abs(g*g>c)>0.0001):
        g += 0.0001
        i = i+1
        print ("%d:g = %.5f"%(i,g))
square_root()
#5牛顿方法c = 2and c = 2000
def square_niudun ():
        c = 2000
        g = c/2
        i= 0
        while(abs(g*g-c>0.0000001)):
        g = (g+c/g)/2
        i = i+1
        print ("%d:%.13f"%(i,g))
square_niudun()
#6
#无影响
#7三次方跟
def square_third():
        c =10
        k = c/3
        while(abs(g**3>0.00001)):
            k = k-(k*k*k-c)/(3*k*k)
        return k
square_third()




#8.1 蒙特卡洛
from random import random
from math import sqrt
from time import perf_counter
DARTS = 10000000
hit = 0.0
perf_counter()
for i in range(1,DARTS+1):
    x = random()
    y = random()
    dist = sqrt(x**2+y**2)
    if dist<=1.0:
        hit = hit+1
pi = 4*(hit/DARTS)
print(pi)
print(perf_counter())
#8.2公式法
pi = 0
N = 100
perf_counter()
for i in range(N):
    pi = pi+1/pow(16,i)*(4/(8*i+1)-2/(8*i+5)-1/(8*i+6))
print(pi)
print(perf_counter())
#8.3无穷级数法
def pi(error):
    a = 1
    b = 1
    sum = 0
    while 1/b>error:
        if a%2!=0:
            sum+=1/b
        else:
            sum-=1/b
        a+=1
        b+=2
    pi = sum*4
    return pi
perf_counter()
p = pi(0.0001)
print(p)
print(perf_counter())
#9 蒙特卡洛求定积分
    from random import random
    from math import sqrt
    from time import perf_counter
    import math
    DARTS = 10000000
    hit = 0.0
    for i in range(1, DARTS + 1):
        x = random.uniform(2,3)
        y = random.uniform(0,30)
        if y<x*2+4*x*math.sin(x):
            hit = hit + 1
    count =  (hit / DARTS)*30
    print(count)
    #
