number = input("정수를 입력해주세요.")
number = int(number)

if number % 2 == 0:
    print("{}는 2로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}는 2로 나누어 떨어지는 숫자가 아닙니다.".format(number))
    
if number % 3 == 0:
    print("{}는 3로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}는 3로 나누어 떨어지는 숫자가 아닙니다.".format(number))
    
if number % 4 == 0:
    print("{}는 4로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}는 4로 나누어 떨어지는 숫자가 아닙니다.".format(number))
    
if number % 5 == 0:
    print("{}는 5로 나누어 떨어지는 숫자입니다.".format(number))
else:
    print("{}는 5로 나누어 떨어지는 숫자가 아닙니다.".format(number))
