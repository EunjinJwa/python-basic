import datetime


now = datetime.datetime.now()

date_str = f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초"
print(date_str)
print(now.date)


