# format{} 함수로 숫자를 문자열로 변환
string_a = "{}".format(10)

# 출력
print(string_a)
print(type(string_a))

format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)
format_d = "{} {} {}".format(1, "문자열", True)

# 출력

print(format_a)
print(format_b)
print(format_c)
print(format_d)