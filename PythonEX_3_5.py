number = input("정수 입력: ")

number = int(number)

#마지막 자리의 숫자를 문자열을 이용해 추출
# last_character = number[-1]

# last_character = int(last_character)

# 원래 끝자리의 숫자를 보고 짝수 홀수 판단이나 귀찮아서 2로 나눠떨어지면 짝수인걸로

if number%2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")