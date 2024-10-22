#여러 줄 문자열과 if조건문 조합

# 1. \n과 괄호로 문자열 연결 
number = int(input("정수 입력:"))

if number % 2 == 0 :
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은 짝수입니다."
    ).format(number, number))
else:
    print((
        "입력한 문자열은 {}입니다.\n"
        "{}은 홀수입니다."
    ).format(number, number))

# 2. join()함수 사용    문자열.join(문자열로 구성된 리스트)  리스트의 요소를 문자열로 연결한다.

number = int(input("정수 입력:"))

if number % 2 == 0:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 짝수입니다."
    ]).format(number, number))
else:
    print("\n".join([
        "입력한 문자열은 {}입니다.",
        "{}은 홀수입니다."
    ]).format(number, number))