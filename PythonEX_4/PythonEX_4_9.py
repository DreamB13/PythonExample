# for문 반대로 반복
for i in range(4,0-1,-1):
    print(f"현재 반복 변수: {i}")

for i in reversed(range(0,5)):
    print(f"현재 반복 변수: {i}")


# 직각삼각형 만들기

height = int(input("몇 줄까지 만들까요? >"))

for i in range(height):
    for j in range(i):
        print("*",end="")
    print("*")