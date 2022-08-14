# 문자열을 숫자로 변환하기 : int(), float()

str_a = input("입력A > ")
int_a = int(str_a)

str_b = input("입력B > ")
int_b = int(str_b)

str_c = "34.997"
float_c = float(str_c)

print("문자타입의 숫자 연산 : ", str_a + str_b)
print("int 변환한 숫자 연산 : ", int_a + int_b)
print("float 변환 : " , float_c)


# 숫자를 문자열로 변환하기 : str()
print(str(33))
print(str(33.564))


# [예제] inch 단위를 cm 단위로 변경하기
raw_input = input("inch 단위의 숫자를 입력해주세요.")
inch = int(raw_input)
cm = inch * 2.54

print(inch, "inch => ", cm, "cm")
print("cm의 타입 : ",type(cm))
