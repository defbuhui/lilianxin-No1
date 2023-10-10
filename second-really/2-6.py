#g = c/2
def Square_root_3_1():
    c = 2
    g = c/2
    i = 0
    while(abs(g*g-c)>0.0000000001):
        g = (g+c/g)/2
        i = i+1
    print("%d:%.13f"%(i,g))
Square_root_3_1()
#g = c
def Square_root_3_2():
    c = 2
    g = c
    i = 0
    while(abs(g*g-c)>0.0000000001):
        g = (g+c/g)/2
        i = i+1
    print("%d:%.13f"%(i,g))
#g = c/4
Square_root_3_2()
def Square_root_3_3():
    c = 2
    g = c/4
    i = 0
    while(abs(g*g-c)>0.0000000001):
        g = (g+c/g)/2
        i = i+1
    print("%d:%.13f"%(i,g))
Square_root_3_3()
#g = c/2 和g = c 运行结果都为4次
#g = c/4运行结果为6次