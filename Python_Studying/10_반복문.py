#반복문

#for문
for i in range(1,11,1): #시작값, 종료값+1, 더할 값
    print(i)
#while문
i=0
while i<10:
    print(i)
    i+=1

#1부터 10까지의 합
sum=0
for i in range(1,11,1):
    sum+=i
print(sum)

i=0
sum=0
while i<=10:
    sum+=i
    i+=1
print(sum)

#1 첫 번째 수부터 두 번째 수까지의 합
a=int(input("첫 번째 수: "))
b=int(input("두 번째 수: "))

sum=0
for i in range(a,b+1,1):
    sum+=i
print(sum)

#2 1부터 20까지의 수 중 3의 배수에서 박수
for i in range(1,21,1):
    if i%3==0:
        print("박수")
    else:
        print(i)

#3 1부터 20까지의 수로 3,6,9게임
for i in range(1,21,1):
    if '3' in str(i) or '6' in str(i) or '9' in str(i): #|와 or의 차이?
        print("박수")
    else:
        print(i)

#break
i=0
while 1:
    print(i)
    i+=1
    if i>20:
        break

