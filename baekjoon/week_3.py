# 1번 문제 ------------------------------------------
str = input()
num = int(input())
print(str[num-1])
# 2번 문제 ------------------------------------------
str = input()
print(len(str))
# 3번 문제 ------------------------------------------
num = int(input())
for i in range(num):
    str = input()
    print(str[0]+str[-1])
# 4번 문제 ------------------------------------------
str = input()
print(ord(str))
# 5번 문제 ------------------------------------------
num = int(input())
numbers = input()
sum = 0
if len(numbers) > num or len(numbers) < num:
    print("입력하신 수만큼 문자열을 입력해주세요.")
else:
    for i in range(num):
        sum += int(numbers[i])
    print(sum)
# 6번 문제 ------------------------------------------
alphabet = 'abcdefghijklmnopqrstuvwxyz'
arr = input()
answer = ''
for i in range(len(alphabet)):
    if alphabet[i] in arr:
        answer += str(arr.find(alphabet[i]))+' '
    else:
        answer += '-1 '
print(answer)
# 7번 문제 ------------------------------------------
num = int(input())
for i in range(num):
    arr = ''
    times, string = input().split()
    times = int(times)
    for i in range(len(string)):
        arr+=string[i]*times
    print(arr)
# 8번 문제 ------------------------------------------
string = input().split()
count = 0
for i in string:
    count += 1
print(count)
# 9번 문제 ------------------------------------------
fir, sec = input().split()
fir2 = fir[::-1]
sec2 = sec[::-1]
if fir2 > sec2:
    print(fir2)
elif sec2>fir2:
    print(sec2)
# 10번 문제 ------------------------------------------
string = input()
count = 0
for i in range(len(string)):
    if 65<=ord(string[i])<68:
        count += 3
    elif ord(string[i])<71:
        count += 4
    elif ord(string[i])<74:
        count += 5
    elif ord(string[i])<77:
        count += 6
    elif ord(string[i])<80:
        count += 7
    elif ord(string[i])<84:
        count += 8
    elif ord(string[i])<87:
        count += 9
    else:
        count += 10
print(count)
# 11번 문제 ------------------------------------------
while True:
    try:
        string = input()
        print(string)
    except:
        break
