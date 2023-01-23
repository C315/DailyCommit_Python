#양식문자
'''
%d 정수(십진수)
%f 실수(소숫점)
%g 정수, 실수 (범용, 잘 안씀)
%s 문자열(단어)
%c 문자(a, b, c, 등)
%o 8진수
%x 16진수

두 개 이상 쓸때는 %(a, b) 이런식으로 괄호로 묶어야함
%숫자d,%숫자f : 숫자 뒤 자릿수 표시
%.숫자f : 소숫점 뒤 자릿수(반올림) (.0 = .)
'''
#1
x=21
print("x의 값은 %d입니다."%x)
print("x의 값은 %f입니다."%x)

#2
height=168.5
text= '내 키는 %fcm 입니다.' %height
print(text)

#3
name='최예지'; age=20; weight=62.5
print('내 이름은 %s입니다.' % name)
print('나는 %d살 입니다.' %age)
print('나의 몸무게는 %.2fkg입니다.' %weight)

#4
x=21; y=3
print("%02d와 %02d을/를 곱한 값은 %02d입니다."%(x,y,x*y)) #0 써줬기 때문에 남는 자리 0으로 채움

#5
a=0.3394
b=2940
print("%.2f+%.0f를 출력할거야" %(a,b))
print("%2f를 출력할거야"%b)

#6
print("%d %5d %05d" %(123,123,123))
print("%f %7.1f %7.3f" %(123.45, 123.45, 123.45))
print("%s %10s" %("Python", "Python"))
print("{0:d} {1:5d} {2:05d}".format(123,456,789)) #{a:b}에서 a는 format 뒤 괄호에서 몇 번째 숫자인지