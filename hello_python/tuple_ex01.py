# tuple 
# 리스트와 비슷한 자료형으로, 한 번 결정된 요소는 바꿀 수 없다.

# 튜플 선언하기 
tuple_a = (1,4,6,8)
tuple_b = 1,4,6,8   # 괄호 없이 할당할 수 있다.
a,b,c = (1,4,5)     # 여러 변수에 각 요소의 값을 할당할 수 있다. 
d,e,f = 1,4,5

print("tutle_a : ", tuple_a)    # tutle_a :  (1, 4, 6, 8)
print("tutle_b : ", tuple_b)    # tutle_b :  (1, 4, 6, 8)
print("a : ", a) # 1
print("b : ", b) # 4
print("c : ", c) # 5
print("d : ", d) # 1
print("e : ", e) # 4
print("f : ", f) # 5


# 튜플을 사용하여 변수의 값 교환하기 
var1 = "apple"
var2 = "banana"

var1, var2 = var2, var1 

print(var1)  # banana
print(var2)  # apple 


# 튜플은 함수에서 여러개의 값을 리턴할때 주로 사용된다.
def return_tuple():
    return (10, 20)

result1, result2 = return_tuple()
print(result1)
print(result2)


# tuple을 리턴값으로 사용하는 대표 함수 divmod() : result => (몫, 나머지)
a, b = 50, 7
print(divmod(a, b))  # (7, 1)







