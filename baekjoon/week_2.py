# 반복문 ------------------------------------------
# 1번 문제 ------------------------------------------
num = int(input())

for i in range(9):
    i = i+1
    print(num,'*',i,'=',num*i)
# 2번 문제 ------------------------------------------
time = int(input())
for i in range(time):
    a, b = map(int, input().split())
    print(a+b)
# 3번 문제 ------------------------------------------
num = int(input())
j=0
for i in range(num):
    j += (i+1)
print(j)
# 4번 문제 ------------------------------------------
price = int(input())
kinds = int(input())
total = 0
for i in range(kinds):
    a, b = map(int, input().split())
    total += a*b

if price == total:
    print("Yes")
else:
    print("No")
# 5번 문제 ------------------------------------------
time = int(input())
long = ''
for i in range(time//4):
    long += 'long '
print(long+"int")
# 6번 문제 ------------------------------------------
import sys
data = []
tries = int(input())      # tries에 횟수 입력
for i in range(tries):    # 그 횟수만큼 돕니다.
     data.append(list(map(int,sys.stdin.readline().split())))    #함수로 받은 문자열을 split()으로 나누고 정수로 바꾼다음에 data에 저장합니다.
     answer = data[i][0] + data[i][1]
     print(answer)
# 7번 문제 ------------------------------------------
import sys
data = []
tries = int(input())      # tries에 횟수 입력
for i in range(tries):    # 그 횟수만큼 돕니다.
     data.append(list(map(int,sys.stdin.readline().split())))    #함수로 받은 문자열을 split()으로 나누고 정수로 바꾼다음에 data에 저장합니다.
     answer = data[i][0] + data[i][1]
     print(f"Case #{i+1}:",answer)
# 8번 문제 ------------------------------------------
import sys
data = []
tries = int(input())      # tries에 횟수 입력
for i in range(tries):    # 그 횟수만큼 돕니다.
     data.append(list(map(int,sys.stdin.readline().split())))    #함수로 받은 문자열을 split()으로 나누고 정수로 바꾼다음에 data에 저장합니다.
     answer = data[i][0] + data[i][1]
     print(f"Case #{i+1}: {data[i][0]} + {data[i][1]} =",answer)
# 9번 문제 ------------------------------------------
times = int(input())
star = '*'
add = '*'

for i in range(times):
    print(star)
    star += add
# 10번 문제 ------------------------------------------
times = int(input())
star = '*'
space = " "

for i in range(times):
    print((space*(times-(i+1)))+(star*(i+1)))
# 11번 문제 ------------------------------------------
import sys
data = []

while True:
    data.append(list(map(int,sys.stdin.readline().split())))
    if data[0][0]+data[0][1] == 0:
        break
    print(data[0][0]+data[0][1])
    data = []
# 12번 문제 ------------------------------------------
import sys
data = []

while True:
            try:
             data.append(list(map(int,sys.stdin.readline().split())))
             print(data[0][0]+data[0][1])
             data = []
            except:
             break
# 1차원 배열 ------------------------------------------
# 1번 문제 ------------------------------------------
import sys
data = []
number = int(input())
count = 0

data.append(list(map(int, sys.stdin.readline().split())))

target_num = int(input())

for i in data[0]:
    if i == target_num:
        count += 1
print(count)
# 2번 문제 ------------------------------------------
import sys
numbers = []

times, target_num = map(int, input().split())

data = list(map(int, sys.stdin.readline().split()))

if len(data) == times:
    for i in data:
        if i < target_num:
             numbers.append(i)
else:
    print(times,'만큼 입력해주세요')
for i in numbers:
    print(i , end=' ')
# 3번 문제 ------------------------------------------
import sys
numbers = []

times = int(input())

data = list(map(int, sys.stdin.readline().split()))

if len(data) == times:
    print(min(data), max(data))
else:
    print(times,'만큼 입력해주세요')
for i in numbers:
    print(i , end=' ')
# 4번 문제 ------------------------------------------
array = []
for i in range(9):
    num = int(input())
    array.append(num)
print(max(array))
print((array.index(max(array))+1))
# 5번 문제 ------------------------------------------
baskets, times = map(int,input().split())
basket = []
for j in range(baskets):
    basket.append(0)
for i in range(times):
    i, j, k = map(int,input().split())
    for num_basket in range(i-1,j,1):
        basket[num_basket] = k

for i in basket:
    print(i,end=' ')
# 6번 문제 ------------------------------------------
baskets, times = map(int,input().split())
basket = []
for i in range(baskets):
    basket.append(i+1)
for i in range(times):
    first, second = map(int, input().split())
    extra = basket[first-1]
    basket[first-1] = basket[second-1]
    basket[second-1] = extra

for i in basket:
    print(i, end=' ')
# 7번 문제 ------------------------------------------
list = []
do = []

for i in range(30):
    list.append(i+1)

for i in range(28):
    student = int(input())
    if student in list:
        do.append(student)

for i in list:
    if i not in do:
        print(i, end=' ')
# 8번 문제 ------------------------------------------
data = []
count = 0
values = []

for i in range(10):
    num = int(input())
    data.append(num)
for i in data:
    value = i % 42
    if value not in values:
        count += 1
        values.append(value)
    else:
        continue
print(count)
# 9번 문제 ------------------------------------------
baskets, times = map(int, input().split())
basket = []
for i in range(baskets):
    basket.append(i+1)
for i in range(times):
    first, second = map(int, input().split())
    basket[first-1:second] = basket[first-1:second][::-1]
for i in basket:
    print(i, end=' ')
# 10번 문제 ------------------------------------------
import sys
subjects = int(input())
sum_score = 0
data = list(map(int, sys.stdin.readline().split()))
if len(data) != subjects:
    print('과목 개수만큼 입력해주세요')
else:
    high_score = max(data)
    for i in range(len(data)):
        score = data[i]/high_score*100
        sum_score += score
print(sum_score/subjects)
