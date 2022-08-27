# 반복문으로 파일 한 줄씩 읽기

def calc_bmi(weight, height):
    return int(weight) / ((int(height) / 100) ** 2)

def bmi_result(bmi):
    if bmi >= 25:
        return "과체중"
    if bmi >= 18.5:
        return "정상 체중"
    return "저체중"

with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        # 데이터 검증 후 문제가 있으면 지나감
        if(not name) or (not weight) or (not height):
            continue

        # bmi 계산하기
        bmi = calc_bmi(weight, height)
        result = bmi_result(bmi)

        # 결과 출력하기
        print('\n'.join(["이름: {}", "bmi: {} ({})"]).format(name, bmi, result))


