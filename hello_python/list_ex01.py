# list 

# 리스트 생성 - 여러가지 자료형 타입을 혼합하여 리스트 작성 가능 
list_a = ["문자열", 91, "숫자", 0, "abc", True]
print(list_a[0], type(list_a[0]))    # 문자열 <class 'str'>
print(list_a[1], type(list_a[1]))    # 91 <class 'int'>
print(list_a[1:3])  # [91, '숫자']
print(type(list_a[1:3]))    # <class 'list'>

# 이중 리스트
list_b = [[1,2,3], [4,5,6], [7,8,9]]
print(list_b[0])        # [1, 2, 3]
print(list_b[0][2])     # 3

# 리스트 연산
list_c = [1,2,3]
list_d = [4,5,6]
print(list_c + list_d)  # [1, 2, 3, 4, 5, 6]
print(list_c * 3)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
print("리스트 길이 : ", len(list_d) )

# 리스트에 요소 추가하기 
# append() : 리스트의 마지막 인덱스에 추가하기
# insert() : 추가할 위치를 지정하여 리스트 중간에 추가하기
# extend() : 리스트에 여러 요소를 append함. 
list_e = [1,2,3]
list_e.append(4)
print(list_e)
list_e.insert(0,0)
print(list_e)
list_e.insert(2,1.5)
print(list_e)       # [0, 1, 1.5, 2, 3, 4]

# 비파괴적 리스트 연산. + 연산자로 요소를 더해줄경우 list_e 에는 변화 없음.
list_e2 = list_e + [5,6]
print(list_e2)

list_e.extend([5,6])
print(list_e)


# 리스트 요소 제거하기
# del 키워드 : del 리스트명[인덱스], del 리스트명[from:to]
# pop() : pop(인덱스). 인덱스 생략시 가장 마지막 요소 제거 
# remove() : 값으로 리스트 요소 제거, 중복 제거는 되지 않고, 첫 번째 해당하는 요소를 삭제함. 
list_all = [0,1,2,3,4,5,6,7,8,9]
del list_all[1]
print(list_all)     # [0, 2, 3, 4, 5, 6, 7, 8, 9]

del list_all[6:8]
print(list_all)     # 0, 2, 3, 4, 5, 6, 9]

list_all.pop(1)
print(list_all)     # [0, 3, 4, 5, 6, 9]

list_all.pop()
print(list_all)     # [0, 3, 4, 5, 6]

list_all.remove(3)
print(list_all)     # [0, 4, 5, 6]

list_all.clear()
print(list_all)     # []

# 리스트 슬라이싱 : 단계! 
# 리스트[시작:끝:단계] : 단계만큼 인덱스를 건너뛰어서 선택함
list_all = [0,1,2,3,4,5,6,7,8,9]
print(list_all)
print(list_all[0:7:2])  # 0~7인덱스 사이 요소를 2개씩 건너뛰어서 선택. [0, 2, 4, 6]
print(list_all[::-1])  # 모든 요소를 출력하되, 역순으로 출력 (-) [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list_all[::-2])   # 모든 요소의 역순(-)에서 2개씩 건너뛰어서 출력 [9, 7, 5, 3, 1]


# 정렬 sort()
list_all = [9,1,6,4,2,6]
print("정렬 sort()")
list_all.sort()
print(list_all)
list_all.sort(reverse=True)
print(list_all)


# in / not in 연산자 
list_all = [100,101,102,300,301,302,900]
print("# in / not in 연산자 ")
print("102 in list_all ? ", 102 in list_all)
print("109 in list_all ? ", 109 in list_all)
print("109 not in list_all ? ", 109 not in list_all)
