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