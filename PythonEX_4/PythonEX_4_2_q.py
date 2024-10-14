# 3번 문제 ---------------------------------------------------------------------

numbers = [1,2,8,6,4,5,5,2,1,4,5,6,8,1,2,3,6,4,5,4,7,7,2,9,2,1]
counter = {}

for number in numbers:
    count_num = 0
    counter[number] = count_num
    if number in counter[number]:
        
        
print(counter)

# 4번 문제 ---------------------------------------------------------------------
# character = {
#     "name": "기사",
#     "level": 12,
#     "items": {
#         "sword": "불꽃의 검",
#         "armor": "풀플레이트"
#     },
#     "skill": ["베기", "세게 베기", "아주 세게 베기"]
# }

# for key in character:
#     if type(character[key]) is str:
#         print(key,":",character[key])
#     elif type(character[key]) is int:
#         print(key,":",character[key])
#     elif type(character[key]) is dict:
#         for i in character[key]:
#             print(i,":",character[key][i])
#     elif type(character[key]) is list:
#         for j in character[key]:
#             print(key,":",j)
