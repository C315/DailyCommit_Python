'''
출력할 메시지 뒤에 첨부
\t  탭
\n  엔터
\'  작은 따옴표 출력
\"  큰 따옴표 출력
\\  역슬래시 출력
\b  백스페이스
r"" : 이스케이프문자도 그대로 출력
'''

print("안녕하세요!\t \"")
print("안녕하세요\b \\")

#프린트
print("예지의 계산기")
print('안녕하세요!')

이름="홍길동"
고향="아름다운 서울"

print(이름)
print(고향)
print("5.5+3.14")

university="숭실대학교"
grade="3"
department="글로벌통상학과"
print("저는", university, grade+"학년", department,"입니다.")

print(type('a')) #변수 유형 확인
print(type('a'), type(1), type("Hi"))

print('안나가 "아빠!"라고 말했다.')
print("삶은 복잡하지만, 행복은 '단순'하다.")
print('큰 따옴표(")와',"작은 따옴표(')의 사용법")
print("\n")
print('''그가 말했다. "이제 'what'은 결정되었으니, 'how'에 대해서 이야기해보자."''')
print("\n")
print("Don't be afraid to fail \n실패하는 것을 두려워하지 말아라.")
print("Be afraid not to try \n시도조차 하지 않는 것을 두려워하라")