# 2차원 배열 ------------------------------------------
# 1번 문제 --------------------------------------------
array = []
sum_array = []
lines,num = map(int,input().split())
if lines > 100 or num > 100:
    print("100보다 작거나 같은 수를 입력해주세요")
else:
    for i in range(lines*2):
        numbers = list(map(int,input().split()))
        array.append(numbers)
    for i in range(lines):
        for j in range(num):
            sum = array[i][j] + array[i+lines][j]
            sum_array.append(sum)
    for i in range(len(sum_array)):
        if 
        print(sum_array[i])