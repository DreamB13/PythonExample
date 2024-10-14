# False로 변환되는 값 = None , 0 , 0.0 , 빈 컨테이너( 빈 문자열, 빈 바이트열, 빈 리스트, 빈 튜플, 빈 딕셔너리)
print("# if 조건문에 0을 넣으면")
if 0:
    print("0은 True값이다.")
else:
    print("0은 False값이다.")

print("# if 조건문에 빈 문자열을 넣으면")
if "":
    print("빈 문자열은 True값이다.")
else:
    print("빈 문자열은 False값이다.")