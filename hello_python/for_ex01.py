list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for element in list_of_list:
    for item in element:
        print("item : ", item)
    print("element : ", element)

# 전개연산자 * : 리스트 요소를 전개하여 입력한 것과 같은 효과 
# *리스트 -> 리스트[0], 리스트[1],... 
print(list_of_list[0])      # [1, 2, 3]
print(*list_of_list[0])     # 1 2 3

list_a = [1,4,6,8,9]
for index in range(len(list_a)):
    print(index, " = ", list_a[index])

