# 01 시간초과,, 왜?
"""n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

sorted_list = []
lst = nlist[:] #임시 리스트
for i in range(n): #정렬
    a = min(lst)
    lst.remove(a)
    sorted_list.append(a)

def binary(s, e, n, lst):
    start = s; end = e; num = n; list = lst;
    while start<=end:
        k = (start + end) // 2
        if list[k]==num:
            return k
        if list[k]>num:
            end=k-1
        else:
            start=k+1
    if start>end:
        return -1

for i in mlist:
    if binary(0,n-1,i,sorted_list) == -1:
        print(0)
    else:
        print(1)"""

# 02
"""a, b = map(int, input().split())

for i in range(a,b+1):
    if i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        print(i)"""