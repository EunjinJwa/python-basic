### Python 기본 문법


#### lambda
```python
lambda 매개변수: 리턴값

ex) 
output = filter(lambda x: x < 4, [1,2,3,4,5,6,7])   # [1,2,3]
```

#### 파일
```python
# 파일 열기
파일 객체 = open(문자열: 파일 경로, 문자열: 읽기 모드)

# 파일 닫기
파일 객체.close()
```
* 모드 : w (write 새로쓰기 모드), a (append모드. 뒤에 이어서 쓰기), r (읽기 모드)








