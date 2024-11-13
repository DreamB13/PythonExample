# 2차원 배열 ------------------------------------------
# 1번 문제 --------------------------------------------
array = []
sum_array = []
int_array = []
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
        int_array.append(sum_array)
        sum_array = []
    for i in range(lines):
        for j in range(num):
            print(int_array[i][j], end=' ')
        print()
# 2번 문제 --------------------------------------------
array = []
max_array = []
for i in range(9):
    numbers = list(map(int,input().split()))
    array.append(numbers)
for i in array:
    max_array.append(max(i))
num_max = max(max_array)
num_index = max_array.index(num_max)
print(num_max)
print(max_array.index(num_max)+1, array[num_index].index(num_max)+1)
# 3번 문제 --------------------------------------------
string_array = []
len_string = []
vertical_array = []
for i in range(5):
    array = list(input())
    string_array.append(array)
for i in string_array:
    len_string.append(len(i))
    max_len = max(len_string)
for i in range(max_len):
    for j in range(5):
        if i >= len(string_array[j]):
            continue
        vertical_array.append(string_array[j][i])
for i in range(len(vertical_array)):
    print(vertical_array[i], end='')
# 4번 문제 --------------------------------------------
array = [['1'] * 100 for i in range(100)] # '1'이 100개인 리스트가 100개  [['1','1','1'...],[...],[...],....]
# 주의!!!!! array = [['1']*100]*100 으로 만들면 동일한 리스트 객체에 참조가 되기 때문에 모든 배열에 참조가 된다.
square = []
zero_sum = 0
count = int(input())
for i in range(count):
    x,y = map(int,input().split())
    square.append([x,y,x+10,y+10])          # square [[x,y,x+10,y+10],[...].[...]]
for i in range(count):
    for j in range(square[i][1],square[i][3]):
        array[j][square[i][0]:square[i][2]] = ['0']*10
for i in range(100):
    zero = array[i].count('0')
    zero_sum += zero
print(zero_sum)
# 일반 수학 1 ------------------------------------------
# 1번 문제 ---------------------------------------------
n,b = input().split()
b = int(b)

numbers = int(n,b)
print(numbers)
# 2번 문제 ---------------------------------------------
def convert_to_base(N, B):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    while N > 0:
        remainder = N % B
        result.append(digits[remainder])  # 나머지에 해당하는 문자 추가
        N //= B

    # 결과를 뒤집어 올바른 순서로 출력
    return ''.join(result[::-1])

# 입력 받기
N, B = map(int, input().split())
print(convert_to_base(N, B))
# 3번 문제 ---------------------------------------------
count = int(input())
for i in range(count):
    change = int(input())
    quarter = change//25
    remain = change%25
    dime = remain//10
    remain %= 10
    nickel = remain//5
    remain %= 5
    penny = remain//1
    print(quarter,dime,nickel,penny)
# 4번 문제 ---------------------------------------------
count = int(input())   # 0-2 1-3 2-5 3-9 4-17 5-33 
dot=2
for i in range(count):
    dot += dot-1
dots = dot**2
print(dots)
# 5번 문제 ---------------------------------------------
number = int(input())
length = 1
n = 1
while n < number:
    n+=6*length
    length+=1
print(length)
# 6번 문제 ---------------------------------------------
num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')
# 7번 문제 ---------------------------------------------
A, B, V = map(int, input().split()); # 낮 올 // 밤 내 // 총 길이

if V < A : 
    print(1)
else:
    if (V-A) % (A-B) == 0 :
        print((V-A) // (A-B) +1)
    else :
        print((V-A) // (A-B) +2)