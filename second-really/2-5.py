def Square_root_3_1():
    c = 2
    g = c/2
    i = 0
    while(abs(g*g-c)>0.0000000001):
        g = (g+c/g)/2
        i = i+1
    print("%d:%.13f"%(i,g))
Square_root_3_1()
#c=2时仅仅运行4次
def Square_root_3_2():
    c = 2000
    g = c/2
    i = 0
    while(abs(g*g-c)>0.0000000001):
        g = (g+c/g)/2
        i = i+1
    print("%d:%.13f"%(i,g))
Square_root_3_2()
#c = 2000时运行9次