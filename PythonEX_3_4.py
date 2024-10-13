# 날짜/시간 기능 가져오기
import datetime

now = datetime.datetime.now()

# 오전
if now.hour < 12:
    print("지금은 오전 {}시 입니다.".format(now.hour))

# 오후
if now.hour > 12:
    print("지금은 오후 {}시 입니다.".format(now.hour))

#봄
if 3<=now.month<=5:
    print("오늘은 {}월이며 계절은 봄입니다!".format(now.month))

#여름
if 6<=now.month<=9:
    print("오늘은 {}월이며 계절은 여름입니다!".format(now.month))

#가을
if 9<=now.month<=11:
    print("오늘은 {}월이며 계절은 가을입니다!".format(now.month))

#겨울
if 12==now.month or 1<=now.month<=2:
    print("오늘은 {}월이며 계절은 겨울입니다!".format(now.month))