# 3번 문제 ---------------------------------------------------------------------

# # numbers = [1,2,8,6,4,5,5,2,1,4,5,6,8,1,2,3,6,4,5,4,7,7,2,9,2,1]
# # counter = {}

# # for number in numbers:
# #     a = number
# #     if a == number:
# #         number_count += 1
# #     counter[a] = number_count



# print(counter)

# 4번 문제 ---------------------------------------------------------------------
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str:
        print(key,":",[key])
    elif type(character[key]) is dict:
        print(character[key])
    elif type(character[key]) is list:
        skill = character[key]
        print(character[key],":",skill[])