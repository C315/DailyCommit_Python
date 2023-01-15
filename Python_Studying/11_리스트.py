# list
a=list([1,3,2,4,5])
print(a, type(a))

b=list(range(1,10,3))
print(b)

A = [1, 3, 4, 5, 8, 12]
'''
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
'''
#슬라이싱
a=[1,2,3,4,5]
print(a[1:3])
print(a[3:])

b="hello"
print(b[2:4])
