# 01 Day_04의 틀린 문제
"""txt = input().upper()
dictA = dict()

for i in txt:
    if i in dictA:
        dictA[i]+=1
    else:
        dictA[i]=1

key=txt[0]
for i in dictA.keys():
    if dictA[i]>dictA[key]:
        key=i

n=0
for i in dictA.values():
    if dictA[key]==i:
        n+=1
    if n>=2:
        key="?"
        break

print(key)"""

# 02
"""num = list(map(int, input().split()))
key="mixed"

for i in range(1,9,1):
    if num[i-1] = i:
        continue
    else:
        break
else:
    key="ascending"

for i in range(8,0,-1):
    if num[8-i] = i :
        continue
    else:
        break
else:
    key="descending"


print(key)"""

# 03
"""remainder = list()
num = list()

for i in range(10):
    num.append(int(input()))

for i in num:
    k = i%42
    if k in remainder:
        continue
    else:
        remainder.append(k)

print(len(remainder))"""

# 04
"""n=int(input())

for i in range(n):
    arr=list(input())
    score=1
    answer=0
    for i in arr:
        if i=="O":
            answer+=score
            score+=1
        else:
            answer+=0
            score=1
    print(answer)"""

# 05
test_case = int(input())
for i in range(test_case):
    h, w, n = map(int, input().split())
    hund = n%h
    one = int(n/h+1)
    if one%w == 0:
        hund+=1
        one=1
    room=hund*100+one
    print(room)