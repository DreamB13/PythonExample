# 날짜/시간과 관련된 기능 가져오기
import datetime

# 현재 날짜 구하기
now = datetime.datetime.now()

# 출력
print(now.year, "년",now.month, "월",now.day, "일")
print(now.hour, "시",now.minute, "분",now.second, "초")

# 프로그래밍 언어는 월을 0~11로 출력한다.(문자열 첫번째 글자가 0번째인 규칙을 지키기 위해) 파이썬은 1~12월 그대로 출력한다.

print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))