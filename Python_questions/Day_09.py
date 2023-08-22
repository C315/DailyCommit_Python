# 01: 4중 for문 말고 다른 방법은 없는가?
"""a, b = map(int, input().split())
board = []
min_lst = []

for i in range(a):
    inp = list(input())
    board.append(inp)

for i in range(a-8+1):
    for j in range(b-8+1):
        num1, num2 = 0, 0
        for m in range(i, i+8):
            for n in range(j, j+8):
                if (m+n)%2 == 0:
                    if board[m][n] != "W": num1+=1
                    if board[m][n] != "B": num2+=1
                else:
                    if board[m][n] != "B": num1+=1
                    if board[m][n] != "W": num2+=1
        min_lst.append(num1)
        min_lst.append(num2)

print(min(min_lst))"""

# 02
""" 첫 시도 코드: 이진탐색에서 실패
k, n = map(int, input().split()) #현재 갖고 있는 수, 필요한 수
line_lst = []
answer = 0
for i in range(k):
    line_lst.append(int(input()))

current_length = max(line_lst)

if n==1: answer = current_length

while True:
    if answer!=0 : break
    cut_num=0
    for i in range(k):
        cut_num += line_lst[i] // current_length
    if cut_num >= n:
        answer = current_length
        break
    else:
        current_length = int(current_length/2)

print(answer)"""

"""k, n = map(int, input().split())
lst = []
for i in range(k):
    lst.append(int(input()))

start, end = 1, max(lst)

while start<=end:
    num_of_lines = 0
    pivot = (start+end)//2

    for i in lst:
        num_of_lines += i//pivot

    if num_of_lines < n:
        end = pivot-1
    elif num_of_lines >= n:
        start = pivot+1

print(end)"""



