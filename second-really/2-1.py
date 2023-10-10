#尽可能拆分成3 其次是2 不要拆分成1
def maxmul (n):
   if n%3==0:
        n = n/3
        max = 3**n
   else:
       count =int(n/3)
       if n%3==2:
           max = (3**count)*2
       else:
           max = (3**(count-1))*4
   return int(max)
n =int(input())
print(maxmul(n))
