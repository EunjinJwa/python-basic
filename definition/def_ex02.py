# ----------------------
# 팩토리얼 구하기
# n! = n * (n-1) * (n-2) * ... * 1
# ----------------------

# 1. 반복문으로 팩토리얼 구하기 
def factorial_01(n):
    output = 1
    for value in range(1, n+1):
        output *= value
    return output

print("3! : ", factorial_01(3))
print("4! : ", factorial_01(4))

# 2. 재귀 함수로 팩토리얼 구하기
def factorial_02(n):
    if n == 0:
        return 1
    else:
        return n * factorial_02(n-1)

print("3! : ", factorial_02(3))
print("4! : ", factorial_02(4))


# -------------
#  3. 피보나치 수열 함수 - 딕셔너리를 사용한 메모 
# -------------

dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output

print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))

