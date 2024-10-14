list_a = [1,2,3,4,5]
print("리스트 요소 하나 제거")

# 방법.1 del 키워드
del list_a[1]
print("del list_a[1] => ", list_a)

# 방법.2 pop() 매개변수를 입력하지 않을 시 -1로 취급해 마지막 요소 제거
list_a.pop(2)
print("pop(2) => ", list_a)

list_b = [1,2,3,4,5,6]

del list_b[2:4]
print(list_b)

numbers = [1,2,3,4,5,6,7,8]
# numbers[0:5:2]  시작부터 끝까지 2단계로
print(numbers[0:5:2])
numbers = [1,2,3,4,5,6,7,8]
# numbers[::-1]   음수로 지정하면 반대로 출력
print(numbers[::-1])

# 값으로 제거하기: 리스트.remover(값) => 가장 먼저 발견되는 값 하나만 없앤다. 배열 안에 같은 값을 전부 없애려면 반복문 사용
# 모두 제거하기 => clear()
# 리스트 오름차순 정렬 => sort()
# 내부에 값이 있는지 확인 => in/not in 연산자
