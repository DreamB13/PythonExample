# 2차원 리스트 반복문 한번 사용하기
list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9]
]

for items in list_of_list:    # list_of_list의 요소가 리스트기 때문에 items는 리스트
    print(items)

for items in list_of_list:
    for item in items:
        print(items)

# 전개 연산자 *리스트 를 사용하면 비파괴적으로 요소를 추가할 수 있다.
#append() 사용일 경우
a = [1,2,3,4]
a.append(5)
print(a)        #원래 a 내용이 파괴

a = [1,2,3,4]
b = [*a,5]
print(b)    #a리스트는 그대로 보존
print(*a,5)

a = [1,2,3,4,5]
b = a.copy()
b.append(6)
print(b)