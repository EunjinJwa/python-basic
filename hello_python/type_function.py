# format() 기본
format_a = "{}".format(10)
format_b = "내 이름은 {}입니다.".format("jinny")

print(format_a)
print(format_b)

# format()을 f- 형태로 변경해보기
name = "jinny"
print(f"{10}")
print(f"내 이름은 {name}입니다.")

# format() 으로 특정 칸에 출력하기
print("{:d}".format(52))    # 52
# 특정 칸에 출력하기
print("{:5d}".format(52))  # '   52' (앞 세자리가 공백임)
# 빈 칸을 0으로 채우기
print("{:05d}".format(52))  # 00052


# 부동소수점 자릿수 지정하기 : '.자리수f'
print("{:.2f}".format(34.5678)) # 34.57 (셋째자리 반올림)

# 의미없는 소수점 제거하기 : {:g}
print("{:g}".format(32.0))  # 32
print("{:g}".format(32.30))  # 32.3
print("{:g}".format(32.12)) # 32.12


# 대소문자 변경
print("alPaBet".upper())
print("alPaBet".lower())

# 문자열 양옆 공백 제거 : strip(), rstrip(), lstrip()
print(" 안녕하세요. ")
print(" 안녕하세요. ".strip())
print(" 안녕하세요. ".rstrip())
print(" 안녕하세요. ".lstrip())

# in 연산자 : 문자열 포함 여부 확인
print("안녕" in "안녕하세요")   # True
print("잘자" in "안녕하세요")   # False


