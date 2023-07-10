# 01 Day_05의 못 푼 문제
"""num = int(input())

for i in range(num):
    h, w, n = map(int, input().split())
    # n/h에 대해 몫 = 호수, 나머지 = 층수
    height = n % h
    if height == 0:
        height = h
        weight = int(n/h)
    else:
        weight=int(n/h)+1
    if weight > w:
        height+=1
        weight%=w
    if height > h:
        weight+=1
        height%=h

    answer = height*100+weight
    print(answer)"""

# 02
"""arr = input()

for i in range(97,123,1):
    x = chr(i)
    print(arr.find(x), end=" ")
print("\n")"""

# 03 ???
"""n, m = map(int, input().split())
arr = list()
for i in range(n):
    arr.append(list(input()))

ex1=list()
ex2=list()

for i in range(8):
    for j in range(0,8,2):
        ex1[i][j]="W"
    for j in range(1,8,2):
        ex1[i][j]="B"


num_of_error=list()
for i in range(n-8):
    for j in range(m-8):"""


# 04
"""n = int(input())

score = map(int, input().split())
score=list(score)

M = max(score)

for i in range(n):
    if score[i]==0:
        continue
    score[i] = (score[i] / M) * 100

print(sum(score)/n)"""

# 05
"""n=int(input())

words = dict()
for i in range(n):
    a=input()
    words[a] = len(a)

words = dict(sorted(words.items()))
words = sorted(words.items(), key=lambda x:x[1])
for i, j in words:
    print(i)"""

# 06
"""while True:
    key = ""
    inp = list(input())
    for s in inp:
        key+=s
    if key == "0":
        break
    for i in range(0,len(inp),1):
        if inp[i] == inp[len(inp)-i-1]:
            continue
        else:
            print("no")
            break
    else:
        print("yes")"""