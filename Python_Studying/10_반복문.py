#반복문

#for문
for i in range(1,11,1): #시작값(기본 0), 종료값+1, 더할 값(기본 1)
    print(i, end=" ")
print("\n")

for i in range(50,71,3):
    print(i, end=" ")
print("\n")

for i in range(10,1,-1):
    print(i, end=" ")
print("\n")

for i in range(1,30,1):
    if i%3==0:
        pass
    else:
        print(i, end=" ")
print("\n")

#while문
import time
i=0
while i<10:
    print(i)
    time.sleep(1)
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
        
#4 구구단
for i in range(1,10):
    for j in range(1,10):
        print("%d * %d = %d" %(i,j,i*j), end="\t")
    print("\n")

#break
i=0
while 1:
    print(i)
    i+=1
    if i>20:
        break

while True:
    x=input("입력하세요: ")
    if x=="x" :
        break
    else :
        print(x)

#continue: 반복문 처음으로 돌아감
for i in range(1,22):
    if i%3==0:
        print("박수")
        continue
    else:
        print(i)

#else: 반복문 종료될 때 마지막에 한 번 실행됨(파이썬only)
for i in [3,6,4,2,9]: #왜 list()로 쓰면 안되지?
   if i>10 :
       break
else:
   print("10 이상의 숫자 없음")