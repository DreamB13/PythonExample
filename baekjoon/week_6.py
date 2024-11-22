# 기하: 직사각형과 삼각형 -------------------------------------
# # 1번 문제 ---------------------------------------------------
# a=int(input())
# b=int(input())
# print(a*b)
# # 2번 문제 ---------------------------------------------------
# x,y,w,h = map(int,input().split())
# array = [x,y,w,h,w-x,h-y]
# print(min(array))
# # 3번 문제 ---------------------------------------------------
# x1,y1 = map(int,input().split())
# x2,y2 = map(int,input().split())
# x3,y3 = map(int,input().split())
# x4,y4 = 0,0
# if x1 == x2:
#     x4 = x3
# elif x2 == x3:
#     x4 = x1
# else:
#     x4 = x2

# if y1 == y2:
#     y4 = y3
# elif y2 == y3:
#     y4 = y1
# else:
#     y4 = y2

# print(x4,y4)
# # 4번 문제 ---------------------------------------------------
# num = int(input())
# print(num*4)
# # 5번 문제 ---------------------------------------------------
# count = int(input())
# x_array=[]
# y_array=[]
# for i in range(count):
#     x,y = map(int,input().split())
#     x_array.append(x)
#     y_array.append(y)
# w=max(x_array)-min(x_array)
# h=max(y_array)-min(y_array)
# print(w*h)
# # 6번 문제 ---------------------------------------------------
# a = int(input())
# b = int(input())
# c = int(input())
# if (a+b+c) != 180:
#     print('Error')
# elif a==b or b==c or a==c:
#     if a==b==c:
#         print('Equilateral')
#     else:
#         print('Isosceles')
# else:
#     print('Scalene')
# # 7번 문제 ---------------------------------------------------
# while True:
#     triangle = list(map(int,input().split()))
#     c=max(triangle)
#     triangle.remove(c)
#     a,b=triangle[0],triangle[1]
#     if a+b+c == 0:
#             break
#     if c>=(a+b):
#         print('Invalid')
#     elif a==b or b==c or c==a:
#         if a==b==c:
#             print('Equilateral')
#         else:
#             print('Isosceles')
#     else:
#         print('Scalene')
# 8번 문제 ---------------------------------------------------
triangle = list(map(int,input().split()))
c=max(triangle)
triangle.remove(c)
a,b=triangle[0],triangle[1]
while True:
    if c >= (a+b):
        c -= 1
    else:
        break
