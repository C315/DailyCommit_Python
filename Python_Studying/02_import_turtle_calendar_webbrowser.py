#turtle
import turtle as t
t.shape('turtle')
t.width(10)
t.shapesize(3)
t.color("#8324FF") #rgb컬러: RRGGBB, 16진수로 표현

for i in range(5):
    t.fd(200)
    t.left(72) #각도 만들 때는 외각을 사용해야 함(ex. 삼각형 -> 120도)
'''
t.shape("") #거북이 모양 변화: turtle, circle, square 등
t.shapesize(숫자) #거북이 크기 변화
t.color("") #거북이 색 변화: b, r, g, yellow 등
t.방향(거리) #거북이 이동
'''

import calendar
calendar.prmonth(2021,3)

import webbrowser
검색=input("무엇을 검색하시겠습니까?: ")
a="https://www.google.com/search?q="+검색+""
#+는 앞뒤 내용 붙인다는 내용
webbrowser.open(a) #파이썬과 웹 연결