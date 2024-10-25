# 입출력과 사칙연산	 ---------------------------------------
# 1번 문제 ---------------------------------------
print('Hello World!')

# 2번 문제 ---------------------------------------
a, b = map(int, input().split())
print(a+b)

# 3번 문제 ---------------------------------------
a,b = map(int, input( ).split( ))
print(a-b)

# 4번 문제 ---------------------------------------
a,b = map(int, input( ).split( ))
print(a*b)

# 5번 문제 ---------------------------------------
a,b = map(int, input( ).split( ))
print(a/b)

# 6번 문제 ---------------------------------------
a,b = map(int, input( ).split( ))
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)

# 7번 문제 ---------------------------------------
name = input()
print(name+"??!")

# 8번 문제 ---------------------------------------
year = int(input())
print(year-543)

# 9번 문제 ---------------------------------------
a,b,c = map(int, input().split())
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)

# 10번 문제 ---------------------------------------
a = input()
b = input()

first = int(a)*int(b[2])
second = int(a)*int(b[1])
third = int(a)*int(b[0])
end = int(a)*int(b)
print(first)
print(second)
print(third)
print(end)

# 11번 문제 ---------------------------------------
print("""\
\    /\ 
 )  ( ')
(  /  )
 \(__)|\
""")

# 12번 문제 ---------------------------------------
print("""\
|\_/|
|q p|   /}
( 0 )\"\"\"\ 
|"^"`    |
||_/=\\\__|\
""")
# 조건문 ---------------------------------------
# 1번 문제 ---------------------------------------
a,b = map(int, input().split())
if a<b:
    print("<")
elif a>b:
    print(">")
else:
    print("==")

# 2번 문제 ---------------------------------------
point = int(input())
if point >= 90:
    print("A")
elif point >= 80:
    print("B")
elif point >= 70:
    print("C")
elif point >= 60:
    print("D")
else:
    print("F")
# 3번 문제 ---------------------------------------
year = int(input())
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("1")
else:
    print("0")
# 4번 문제 ---------------------------------------
x = int(input())
y = int(input())
if (x > 0) and (y > 0):
    print("1")
elif (x < 0) and (y > 0):
    print("2")
elif (x < 0) and (y < 0):
    print("3")
else:
    print("4")
# 5번 문제 ---------------------------------------
h, m = map(int, input().split())
if (m-45)>=0:
    print(h, m-45)
elif ((m-45)<0) and ((h-1)<0):
    print(24+(h-1), 60+(m-45))
elif (((m-45)<0) and ((h-1)>=0)):
    print(h-1, 60+(m-45))
# 6번 문제 ---------------------------------------
h,m = map(int, input().split())
timer = int(input())
total = m + timer

if (total)<60:
    print(h, total)
elif total >= 60:
    hours = h + (total//60)
    minuite = total%60
    if hours >= 24:
        hours = hours % 24
    print(hours, minuite)
# 7번 문제 ---------------------------------------
a,b,c = map(int, input().split())
money = 0
list = [a,b,c]
max = int(max(list))

if (a == b) & (b == a) & (c == a):
    money = 10000 + (max*1000)
elif (a != b) & (b != c) & (c != a):
    money = max*100
else:
    if ((a == b) & (a != c)) or ((a == c) & (a != b)):
        money = 1000 + a*100
    elif (b == c) & (b != a):
        money = 1000 + b*100

print(money)