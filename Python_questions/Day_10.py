# 01
"""n = int(input())
num_lst = [int(input()) for x in range(n)]

nums = [x for x in range(1,n+1)]
stack = [0 for x in range(n)]
nums_index = 0
stack_index = -1

normal = 0
answers = []

for i in range(n):
    current = num_lst[i]
    while nums_index < n:
        if nums[nums_index] < current+1:
            answers.append("+")
            stack[stack_index+1] = nums[nums_index]

            nums_index+=1
            stack_index+=1
        else:
            break
    while stack[stack_index] > current:
        answers.append("-")
        stack[stack_index] = 0
        stack_index-=1
    if stack[stack_index] == current:
        answers.append("-")
        stack[stack_index] = 0
        normal+=1
        stack_index-=1

if normal != n:
    print("NO")
else:
    for i in answers:
        print(i)"""

# 02: 시간복잡도 줄이기!!
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

sorted_list = []
lst = nlist[:] #임시 리스트
for i in range(n): #정렬
    a = min(lst)
    lst.remove(a)
    sorted_list.append(a)

def binary(start, end, n, list):
    k = (start+end)//2
    if start>end:
        return -1
    else:
        if list[k] == n:
            return k
        elif list[k]>n:
            return binary(start, k-1, n, list)
        else:
            return binary(k+1, end, n, list)

for i in mlist:
    if binary(0,n-1,i,sorted_list) == -1:
        print(0)
    else:
        print(1)