# 약수, 배수와 소수 ------------------------------------------
# # 1번 문제 --------------------------------------------
# while True:
#     a,b = map(int,input().split())
#     if a==0 and b == 0:
#         break
#     else:
#         if b % a == 0:
#              print('factor')
#         elif a % b == 0:
#             print('multiple')
#         else:
#             print('neither')
# # 2번 문제 --------------------------------------------
# a,b = map(int,input().split())
# array = []
# if b > a or b < 1 or a < 1 or a > 10000:
#     print('오류')
# else:
#     for i in range(1,a+1):
#         if (a % i) == 0 :
#             array.append(i)
#     for i in range(a-len(array)):
#         array.append(0)
#     print(array[b-1])
# # 3번 문제 --------------------------------------------
# while True:
#     num = int(input())
#     if num == -1:
#         break
#     array =[]
#     for i in range(1,num):
#         if (num % i) == 0:
#             array.append(i)
#     if sum(array) == num:
#         print(f'{num} = ',end='')
#         for i in array:
#             if i == array[-1]:
#                 print(i)
#                 continue
#             print(f'{i} + ',end='')
#     if sum(array) != num:
#         print(f'{num} is NOT perfect.')
# 4번 문제 ----------------------------------------------
count = int(input())
if count > 100:
    print('error')
else:
    