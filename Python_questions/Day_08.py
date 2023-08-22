# 01
"""n = int(input())

if n == 0:
    answer=0
else:
    num=n

    for i in range(n-1,0,-1):
        num*=i

    num = list(str(num))

    answer=0

    for i in range(len(num)-1,-1,-1):
        if num[i]=="0":
            answer+=1
        else:
            break

print(answer)"""

# 02
"""n = int(input())

numbers=list()

numbers.append(int(input()))

for i in range(n-1):
    n = int(input())
    while n > numbers[len(numbers)-1]:
        """
