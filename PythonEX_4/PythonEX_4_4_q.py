# 2번 문제 ------------------------------------------
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character= {}
for i in range(4):
    character[key_list[i]] = value_list[i]

print(character)
# 3번 문제 -----------------------------------------
limit = 10000
i = 1
sum_value = 0
while sum_value < limit:
    sum_value += i
    i += 1

print("{}를 더할 때 {}을 넘으며 그때의 값은 {}입니다.".format(i-1, limit, sum_value))
# 4번 문제 ----------------------------------------
max_value = 0
a = 0
b = 0
for i in range(100): 
    j = 100 - i
    if j*i>max_value:
        max_value = j * i
        a = j
        b = i
print("최대가 되는 경우: {} * {} = {}".format(a,b,max_value))