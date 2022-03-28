people = 9
apple = 20

# 조건문 
# if 조건이 충족한다면, 그 아래 들여쓰기 한 코드가 실행이 된다. (들여쓰기가 없다면 error 발생)
if people < apple / 5:
    print('gogo')
else :
    print('chuchu')


# 조건문 블럭 작성하기 
if True:
    print('조건문 블럭 시작')
    print('................')

    if True:
        print('참 입니다.')
    if False:
        print('거짓 입니다.')

print('조건문 블럭 종료')


# if / else 
SCISSOR = '가위'
ROCK = '바위'
PAPER = '보'

WIN = '이김'
DRAW = '비겼음'
LOSE = '졌다.'

mine = '가위'
yours = '바위'

if mine == yours:
    result = DRAW
else:
    if mine == SCISSOR:
        if yours == ROCK:
            result = LOSE
        else:
            result = WIN
    else:
        if mine == PAPER:
            if yours == SCISSOR:
                result = LOSE
            else:
                result == WIN
print("1) 결과는 ? {}".format(result))        

# if / else: if ... 는 if / elif 로 변경 가능하다.

if mine == yours:
    result = DRAW
elif mine == SCISSOR:
    if yours == ROCK:
        result = LOSE
    else:
        result = WIN
elif mine == PAPER:
    if yours == SCISSOR:
        result = LOSE
    else:
        result == WIN
print("2) 결과는 ? {}".format(result)) 



