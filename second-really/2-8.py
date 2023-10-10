import math
import random
import time
def calculate_pi_1():
    hits = 0
    for i in range(0,1000000):
        x,y = random.random(),random.random()
        dist = math.sqrt(x*x+y*y)
        if dist<=1.0:
            hits+=1
    pi = 4*(hits/1000000)
    print(pi)
start_1 = time.perf_counter()
calculate_pi_1()
end_1 = time.perf_counter()
print(end_1-start_1)
def calculate_pi_2():
    e = 0.0001
    x = 0
    n = 1
    while True:  # 不断循环去找出条件符合的结果
        x = x + pow(-1, n + 1) * (1 / (2 * n - 1))  # 格雷戈里公式
        if (e > abs(1 / (2 * n - 1))):
            break  # 满足条件跳出循环
        else:
            n += 1
    print(x * 4)
start_2= time.perf_counter()
calculate_pi_2()
end_2= time.perf_counter()
print(end_2-start_2)
#第三种
pi = math.pi
print(pi)
