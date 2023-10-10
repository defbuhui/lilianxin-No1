import math
import random
def calculate ():
    count = 0
    for i in range (1,10000):
        x,y = random.uniform(2,3),random.uniform(0,20)
        if y<x*x+4*x*math.sin(x):
            count+=1
    result = count/10000*20
    print(result)
calculate()