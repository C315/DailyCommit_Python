#elif : else if 줄임말
#조건문 표현: 콜론(:) 사용, 들여쓰기, if 뒤 괄호 자유

#1 성적별 학점 출력
score=int(input("성적을 입력하세요: "))

if score>=90 :
    print("A 학점 입니다.")
elif score>=80 :
    print("B 학점 입니다.")
elif score>=70 :
    print("C 학점 입니다.")
else :
    print("Fail 입니다.")
print("수고하셨습니다.")

#2 출생년도로 나이 확인
year=int(input("출생 년도를 입력하십시오: "))
age=2023-year+1

if 1<age<=7 :
    print("어린이", end=" ")
elif age<=13 :
    print("초등학생", end=" ")
elif age<=16:
    print("중학생", end=" ")
elif age<=19:
    print("고등학생", end=" ")
else :
    print("성인", end=" ")
print("이군요! ")

#3 한국 시간으로 프랑스 시간 계산
print("한국의 시간을 입력하십시오")
Kh=int(input())
print("시", end=" ")
Km=int(input())
print("분")