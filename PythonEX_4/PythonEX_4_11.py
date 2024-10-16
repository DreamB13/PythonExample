# while 반복문 기본
i = 0
while i < 10:
    print(f"{i}번째 반복문")
    i += 1



list = [1,2,1,2]
value = 2
while value in list:
    list.remove(value)

print(list)