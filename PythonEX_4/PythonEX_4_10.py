# 피라미드 만들기 no.1
height = int(input("몇 줄까지 만들까요? >"))

for i in range(height):
    for j in range(height-i):
        print(" ",end="")
    for k in range((i*2)+1):
        print("*",end="")
    print("")
