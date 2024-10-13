print("3+4 = " + str(3+4)) # 만약 str로 묶지 않는다면 문자열 연결 연산인지 숫자 덧셈인지 인식하지 못함.

# format()를 이용한 방법
sum = "3+4 = {}".format(3+4)
print(sum)

# format()  => f-문자열: f'문자열{표현식}문자열'
fsum = f'{10}'
fsum2 = f"3 + 4 = {3+4}"
fsum3 = f"""1 + 2 = {1+2}
            2 + 3 = {2+3}
            3 + 4 = {3+4}"""

print(fsum)
print(fsum2)
print(fsum3)