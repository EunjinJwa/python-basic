# 자료형 

# 문자열.format =====================================

number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = 'Welcome'

# 단순 문자열 나열하는 방법
print(number, '번 손님, ', greeting, '.', place, '에 오신것을 환영합니다. ', welcome)

# format 지정 방법
base = '{}번 손님, {}. {}에 오신 것을 환영합니다. {}'
new_format = base.format(number, greeting, place, welcome)

print(base)
print(new_format)


# 문자열을 표현하는 따옴표 
# 싱글 따옴표, 쌍따옴표 모두 문자열을 표현할 수 있다.

# 따옴표 3개 사용하기
line_string = '''첫째줄은 좋은데
둘째줄도 표현 가능'''
print(line_string) 

quote1 = "가끔은 '와 " + '"을 모두 쓰기도 한다.'
quote2 = """가끔은 '와 "을 모두 쓰기도 한다."""     # 더하기 기호 없이 따옴표 기호를 문자열 안에 넣을 수 있음
print(quote1)
print(quote2)

