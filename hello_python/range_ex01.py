# range

a = range(5)
print(a)  # range(0,5)
print(list(a)) # [0,1,2,3,4]

b = range(5,10)
print(list(b)) # [5,6,7,8,9]
for item in range(5,10):
    print("b item : ", item)

# 0부터 (10-1) 까지 3씩 증가하는 수
c = range(0,10,3)
print(list(c)) # [0,3,6,9]

# range 역순, 역 반복문 : range(from, to, -1)
print(list(range(4,0,-1)))
for i in range(4, 0, -1):
    print(i)


## [예제] 피라미드 만들기!
for line in range(1,10):
    print("*"*line)

print()

for line in range(1,10):
    star = ""
    for item in range(line):
        star += "*"
    print(star)
