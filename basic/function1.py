# 함수 정의 
from audioop import add


def function():
    print('Hi, function! ')

function()

def add_10(value):
    "value에 10을 더한 값을 리턴하는 함수"
    result = value + 10
    return result

n = add_10(40)
print(n)


# 함수에서 여러 값 return하기

def root(a, b, c):
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2 # return에 콤마를 이용하여 여러 값을 한 번에 리턴할 수 있음

x=1
y=2
z=-8

r1, r2 = root(x, y, z)
print('근은 {} {}'.format(r1, r2))