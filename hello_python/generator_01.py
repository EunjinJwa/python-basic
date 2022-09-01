# generator 와 next() 함수

def test():
    print("A Pass")
    yield 1
    print("B Pass")
    yield 2
    print("C Pass")
    yield 3

output = test()

print("시작한다!")

a = next(output)
print(a)
print("E Pass")
b = next(output)
print(b)
print("F Pass")
c = next(output)
print(c)
next(output)

