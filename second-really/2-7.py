def Cubic_root():
    c = 10
    g = c/3
    i = 0
    while(abs(g*g*g-c)>0.0000000001):
        g = g - (g*g*g-c)/(3*g*g)
        i = i+1
    print("%d:%.13f"%(i,g))
Cubic_root()