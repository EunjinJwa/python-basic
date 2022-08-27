# 파일 쓰기 : write()

file = open("temp/basic.txt", "w")

file.write("Hello Python new text file.!! ")
file.write("줄바꿈 처리가 되어 작성되지는 않는다. ")
file.writelines("그렇다면 writelines 함수는 줄바꿈처리가 될까? => 안됨")
file.writelines("\n수동으로 줄바꿈?! => 요건 먹히네")

file.write("\n")

list_a = ["리스트를", "write 한다면?", " 요것도 줄바뀜은 안먹힘"]
file.writelines(list_a)

file.close()

# with 구문을 사용
with open("temp/basic.txt", "a") as file:
    file.write("with 키워드를 사용하면, with구문이 종료될 때 자동으로 파일이 닫힙니다.\n")

# 줄바꿈
with open("temp/basic.txt", "a") as file2:
    line_1 = "1. 라인 요소소를 각각 writelines() 함수 인자값의 list인자로 넘기면"
    line_2 = "줄바뀜 안됩니다..ㅎㅎ"

    file2.writelines(["\n",line_1, line_2])







