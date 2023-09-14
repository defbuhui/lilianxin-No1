#2
print("Hello Word")
#3
print("李莲鑫"+"10225501413")
#4
print(chr(0x2605)*11)
print(chr(0x2605)*1+"数据科学与工程导论"+chr(0x2605)*1)
print(chr(0x2605)*11)
#5从小到大输出x,y,z
x = input("请输入第一个数字")
y = input("请输入第二个数字")
z = input("请输入第三个数字")
if x>y:
    a = y
    y = x
    x = a
if x > z:
    a = z
    z = x
    x = a
if y > z:
    a = z
    z = y
    y = a
print(f"x y z从小到大的顺序是{x}，{y}，{z}")
#6从大到小输入a,b,c,d
a = input("请输入第一个数字")
b = input("请输入第二个数字")
c = input("请输入第三个数字")
d = input("请输入第四个数字")
"""
list = [x,y,z,w]1
list.sort()
print(f"从大到小为{list}")
a = {"x":x,"y":y,"z":z,"w":w}
for m in sorted(a,key = a.get):
    print(a[m],end = '')
"""
if b>a:
    temp = b
    b = a
    a = temp
if d>c:
    temp = d
    d = c
    c = temp
if c>a:
    temp = c
    c = a
    a = temp
if c>b:
    temp = c
    c = b
    b = temp
if d>c:
    temp = d
    d = c
    c = temp
print(f"这四个数从大到小为{a},{b},{c},{d}")
#7输出100以内奇数
for i in range(1,101,2):
    print(i,end=' ')
#8 1加到100的和
add = 0
for count in range(0,100):
    add +=count
print(add)
#9 到排序输出
"""
L = [1,2,3,4,5]
N= [1,2,3,4,5]
count = 0
while count <5:
    N[4-count] = L[count]
    count+=1
print(N)

L = [1,2,3,4,5]
print(sorted(L,reverse = True))
"""
L = [1,2,3,4,5]
New_L = []
i = len(L)-1
while i>=0 :
    New_L.append(L[i])
    i-=1
print(New_L)

#10 判断是否有连续相同的字符
count= 0
str = input("请输入一个字符串：")
while count<len(str)-1:
    if str[count]==str[count+1]:
        print("YES")
        break
    count+=1
if count==len(str)-1:
    print("NO")

#11 求去除空格
str = input("请输入一个字符串：")
print(str.replace(" ",""))
#12 求三次方根
count = int(input("请输入一个数字："))
sqrt_count= count**(1/3)
print(f"三次方根为{sqrt_count}")
#13 求乘阶
count = 1
digit = int(input("请输入一个数字："))
for letter in range(1,digit+1):
    count= count*letter
print(f"{digit}的乘阶为{count}")
