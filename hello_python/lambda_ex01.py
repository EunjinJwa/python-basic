# lambda 
# 함수를 매개변수로 전달할 수 있게 작성할 수 있는 기능 

# =======================
# 람다를 사용하지 않고 매개변수로 함수를 전달해서 사용하는 방법 
# =======================

# 함수 선언
def power(item):
    return item * item

def under_3(item):
    return item < 3

# 변수 선언
list_input_a = [1,2,3,4,5]

# map() 함수 사용
output_a = map(power, list_input_a)
print("# map() 함수의 실행 결과")
print("map(power, list_input_a) : ", output_a)  # [1, 4, 9, 16, 25]
print(list(output_a))
print()

# filter() 함수 사용하기 
output_b = filter(under_3, list_input_a)
print("# filter() 함수 실행 결과")
print(output_b)
print(list(output_b))       # [1, 2]



# =======================
# 람다를 사용해서 작성하는 방법
# =======================

# 함수 선언
power_l = lambda x: x * x
under_3_l = lambda x: x < 3

# 변수 선언
list_input_b = [1,2,3,4,5]

# map()
output_c = map(power_l, list_input_b)
print(list(output_c))   # [1, 4, 9, 16, 25]

# filter()
output_d = filter(under_3_l, list_input_b)
print(list(output_d)) # [1, 2]

# =======================
# 람다 함수를 선언하지 않고 바로 사용하기 
# =======================

output_e = map(lambda x: x * x, list_input_a)
output_f = filter(lambda x: x < 3, list_input_a)

print(list(output_e))   # [1, 4, 9, 16, 25]
print(list(output_f))   # [1, 2]

output = filter(lambda x: x < 4, [1,2,3,4,5,6,7])
print(list(output))