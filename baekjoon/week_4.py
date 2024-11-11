# 2차원 배열 ------------------------------------------
# # 1번 문제 --------------------------------------------
# array = []
# sum_array = []
# int_array = []
# lines,num = map(int,input().split())
# if lines > 100 or num > 100:
#     print("100보다 작거나 같은 수를 입력해주세요")
# else:
#     for i in range(lines*2):
#         numbers = list(map(int,input().split()))
#         array.append(numbers)
#     for i in range(lines):
#         for j in range(num):
#             sum = array[i][j] + array[i+lines][j]
#             sum_array.append(sum)
#         int_array.append(sum_array)
#         sum_array = []
#     for i in range(lines):
#         for j in range(num):
#             print(int_array[i][j], end=' ')
#         print()
# # 2번 문제 --------------------------------------------
# array = []
# max_array = []
# for i in range(9):
#     numbers = list(map(int,input().split()))
#     array.append(numbers)
# for i in array:
#     max_array.append(max(i))
# num_max = max(max_array)
# num_index = max_array.index(num_max)
# print(num_max)
# print(max_array.index(num_max)+1, array[num_index].index(num_max)+1)
# 3번 문제 --------------------------------------------
string_array = []
length = []
vertical_array = []
for i in range(5):
    array = list(input())
    string_array.append(array)

for i in string_array:
    length.append(len(i))

