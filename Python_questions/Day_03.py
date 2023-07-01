# 1
"""lista = []

for i in range(9):
    lista.append(int(input()))

a = max(lista)
print(a)
print(lista.index(a)+1)"""

# 2
"""a = int(input())
for i in range(a):
    n, char = input().split()

    char=list(char)
    n = int(n)

    for j in range(len(char)):
        print(char[j]*n, end="")
    print(end="\n")
"""

# 3
"""a = int(input())
lista = list(map(int, input().split()))

print(min(lista), end=" ")
print(max(lista))"""

# 4
"""a = int(input())
b = list(input())
num=0
for i in range(a):
    num+=int(b[i])

print(num)"""

# 5
"""char = input().split()
print(len(char))"""