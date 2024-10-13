# 날짜/시간 기능 가져오기
import datetime

now = datetime.datetime.now()

# 오전
if now.hour < 12:
    print("지금은 오전 {}시 입니다.".format(now.hour))

# 오후
if now.hour > 12:
    print("지금은 오후 {}시 입니다.".format(now.hour))