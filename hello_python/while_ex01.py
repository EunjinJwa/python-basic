# while

import time


i = 0
while i < 10:
    print(i, ", ", end="")
    i += 1

print()

list_a = [1,5,2,7,2,5,2]
while 2 in list_a:
    list_a.remove(2)
print(list_a)

# unix time을 사용해서 5초동안 반복하기
number = 0
target_tick = time.time() + 5
while time.time() < target_tick:
    number += 1
print("5초 동안 반복 횟수 : ",number)

# break 키워드
i = 0
while True:
    print(f"{i} 번째 반복입니다.")
    i += 1
    answer = input("stop 하시겠습니까? (y/n)")
    if answer in ["yes", "y", "Y"]:
        print("반복을 종료합니다.")
        break
