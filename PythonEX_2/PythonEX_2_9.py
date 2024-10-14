# 점수
output_a = "{:d}".format(52)           # {:d}는 int 자료형의 정수만 출력

# 특정 칸에 출력하기
output_b = "{:5d}".format(52)
output_c = "{:10d}".format(52)

# 빈 칸을 0으로 채우기
output_d = "{:05d}".format(52)
output_e = "{:05d}".format(-52)

print("# 기본")
print(output_a)
print("# 특정 칸에 출력")
print(output_b)
print(output_c)
print("# 빈칸을 0으로 채우기")
print(output_d)
print(output_e)

# 기호와 함께 출력
output_f = "{:+d}".format(52)        # 양수
output_g = "{:+d}".format(-52)       # 음수
output_h = "{: d}".format(52)        # 양수: 기호 부분 공백
output_i = "{: d}".format(-52)       # 양수: 기호 부분 공백

print("# 기호와 함께 출력하기")
print(output_f)
print(output_g)
print(output_h)
print(output_i)