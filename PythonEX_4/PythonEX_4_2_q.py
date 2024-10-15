# 3번 문제 ---------------------------------------------------------------------

numbers = [1,2,8,6,4,5,5,2,1,4,5,6,8,1,2,3,6,4,5,4,7,7,2,9,2,1]
counter = {}

for number in numbers:
        count = 0
        counter[number] = count
        base = number
        for i in numbers:
                if base == i:
                        count += 1
                        counter[number] = count
print(counter)

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
        print(key,":",character[key])

    elif type(character[key]) is int:
        print(key,":",character[key])

    elif type(character[key]) is dict:
        for i in character[key]:
            print(i,":",character[key][i])

    elif type(character[key]) is list:
        for j in character[key]:
            print(key,":",j)

# 3번 문제 정답---------------------------------------------------------------------
numbers = [1,2,8,6,4,5,5,2,1,4,5,6,8,1,2,3,6,4,5,4,7,7,2,9,2,1]
counter = {}

for number in numbers:
     if number in counter:
          counter[number] = counter[number] + 1
     else:
          counter[number] = 1

print(counter)

# 4번 문제 정답 ---------------------------------------------------------------------
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
     if type(character[key]) is dict:
          for small_key in character[key]:
               print(small_key,":",character[key][small_key])
     elif type(character[key]) is list:
          for item in character[key]:
               print(key,":",item)
     else:
          print(key,":",character[key])