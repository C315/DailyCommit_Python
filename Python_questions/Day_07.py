# 01: Day_06에서 틀린거 다시
# ?????
"""a, b = map(int, input().split())
board = list()
for i in range(a):
    board.append(list(input()))

numbers = list()

for i in range(a-7):
    for j in range(b-7):


def Calculation(lst):
    for i in range(8):
        if i%2==0:"""


# 02
"""n = int(input())
k=0; num=0;

while True:
    if k==n:
        print(num)
        break
    num+=1
    if "666" in str(num):
        k+=1"""

# 03 ?
"""k, n = map(int, input().split())
lst=list()"""

# 04 ?
n=int(input())

num = map(lambda x : x*(x-1), range(n,0,-1))

num = list(str(num))

answer=0

for i in range(len(num), -1, -1):
    if num[i] == "0":
        print(answer)
    else:
        answer+=1
