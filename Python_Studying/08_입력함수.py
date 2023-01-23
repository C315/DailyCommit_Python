#입력함수
'''
a=input("")꼴로 입력받을 수 있음(""에는 질문/입력 지시 가능)
기본적으로 문자열로 입력받음
변환
    int(): 정수값으로 변환
    float(): 실수값으로 변환
    str(): 문자열로 변환
'''


#1 인사하기
print("이름 입력: ", end=" ")
name=input()
print("안녕!", name,"씨 반가워요!")

#2 고향
home=input("고향 입력: ")
print("아름다운", home,"출신이시군요!")

#3 색깔 및 동물
color=input("무슨 색을 좋아하시나요? ")
animal=input("어떤 동물을 좋아하시나요? ")
print("그럼",color,animal,"을/를 좋아하시겠네요!")

#4 택배 배송 정보
print("택배 배송을 위한 정보를 입력하세요: ")
a=input("1) 받는 분 이름: ")
b=input("2) 받는 분 연락처: ")
c=input("3) 받는 분 주소: ")
d=input("4) 배송 메시지: ")

print("\n아래 정보로 배송하겠습니다.")
print("===============================")
print("- 받는 분 이름: %s" %a)
print("- 받는 분 연락처: %s" %b)
print("- 받는 분 주소: %s" %c)
print("- 배송 메시지: %s" %d)
print("===============================")

#5 연산
a=int(input("연산자를 고르세요: \n1. 덧셈 2. 뺄셈 3. 곱셈 4. 나눗셈"))
b=int(input("첫 번째 수를 입력하세요: "))
c=int(input("두 번째 수를 입력하세요: "))

if a==1:
    print(b+c)
if a==2:
    print(b-c)
if a==3:
    print(b*c)
if a==4:
    print(b/c)