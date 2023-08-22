# 01
n = int(input())
nums = [x for x in range(n)]
stack = []
current_index = 0

for i in range(n):
    current = int(input())
    if nums[current_index] < current:
        stack.append(nums[current_index])
        current_index+=1
    elif nums[current_index] == current:
        print("pop")
        current_index-=1