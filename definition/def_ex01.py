def print_intro():
    print("hello")
    print("python!")

def print_hello(name):
    print(name, "님")
    print("hello!")

print_intro()
print_hello("jinny")


# 기본 매개변수 : default값을 지정하여 필수로 전달받지 않아도 되는 매개변수
def test(a, b=10, c=10):
    print(a+b+c)

test(100)
test(100, b=1)
test(100, 1)
test(100, 1, 20)

def test_return(a, b=10, c=10):
    return a + b + c

# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print(sum_all(1,5))


def mul(*values):
    output = 1
    for value in values:
        output *= value
    return output

print(mul(5,7,9,10))

