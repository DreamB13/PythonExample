import datetime

hello = input("입력: ")
now = datetime.datetime.now()
hour = now.hour

if hello in "안녕하세요":
    print("안녕하세요.")

if hello in "지금 몇 시야?" or hello in "지금 몇 시에요?":
    print("지금은 {}시 입니다.".format(hour))