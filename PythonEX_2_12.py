# 소수 자릿수 지정

output_a = "{:15.3f}".format(52.273)
output_b = "{:15.2f}".format(52.273)
output_c = "{:15.1f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)          # 반올림을 하기 때문에 0.27이 0.3으로 출력됨

# 의미 없는 소수점 제거하기 예. 0.0
output_d = 52.0
output_e = "{:g}".format(output_d)
print(output_d)
print(output_e)