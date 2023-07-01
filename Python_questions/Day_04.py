# 01
a = input().upper()
b = dict()

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

key=a[0]
for i in list(b.keys()):
    if i==key:
        continue
    else:
        if b[i]>b[key]:
            key=i

if b[key] in list(b.values()):
    key="?"

print(key)


# 02
"""num=int(input())

for i in range(num):
    print(" " * (num-i-1), end="")
    print("*"*(i+1))"""

# 03
"""num=1
dic = dict()

for i in range(3):
    a=int(input())
    num*=a

num=list(str(num))

for i in num:
    if i in dic.keys():
        dic[i]+=1
    else:
        dic[i]=1

for i in range(10):
    i=str(i)
    if i in dic.keys():
        print(dic[i])
    else:
        print(0)"""

# 04
"""hour, min = map(int, input().split())

if min<45:
    min += 15
    if hour == 0:
        hour = 23
    else:
        hour -= 1
else:
    min -= 45


print(hour, min)"""