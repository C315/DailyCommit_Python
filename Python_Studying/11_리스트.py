# list
a=list([1,3,2,4,5])
print(a, type(a))

b=list(range(1,10,3))
print(b)

A = [1, 3, 4, 5, 8, 12]

#리스트 값 생성
a=[]
for i in range(3):
    a.append(int(input("숫자 입력: ")))
print(a)

a=[0,0,0]
for i in range(3):
    a[i]=int(input("숫자 입력: "))
print(a)

#메소드
b=[1,2,3]
b[1]=[101,202,303]
print(b)
b.insert(3,4) #위치, 값
b.remove(1) #값
b.pop(1) #위치, 해당 위치의 값 출력

a=[1,2,3]
a.reverse(); print(a)
a.sort(); print(a)
print(sorted(a)); print(a)
print(a.count(2)) #값의 개수

del b[1] #값 제거

# 출력
for i in range(len(A)):
    print(A[i], end=" ")
print('\n')

# 리스트 데이터 수정
A[2] = 44
A.append(20)  # 데이터 추가
A.insert(1, 2)  # 위치, 값
print(A)

# 리스트 합치기
a = [1, 3, 5]
b = [2, 4, 6]

a.extend(b)
print(a)

# 예시
scores=[]
while True:
    score=input("점수 입력: ")
    if score=='x':
        break
    else:
        scores.append(int(score))

sum=sum(scores)
ave=sum/len(scores)
print("평균 점수는 %d입니다"%ave)

#리스트 복제
a=[3,7,8,2]
new=a #같은 공간을 공유해서 복제되지 않음
new.append(7)
print(new); print(a)

new2=a[:]#복제
new.append(3)
print(new2); print(a)

#중첩리스트
a=[[1,2],[3,4],[5,6]]
a[2][0]

#중첩리스트 형성 및 출력
list1=[]
list2=[]
value=0

for i in range(3):
    for k in range(4):
        list1.append(value)
        value+=1
    list2.append(list1)
    list1=[]

for i in range(3):
    for j in range(4):
        print("%2d"%list2[i][j], end=" ")
    print("")

#슬라이싱
a=[1,2,3,4,5]
print(a[1:3])
print(a[3:])

print(a[1:4:2]) #(시작값:끝값+1:증감값)

b="hello"
print(b[2:4])
