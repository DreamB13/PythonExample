example_list = ["요소A","요소B","요소C"]

print("# 단순 출력")
print(example_list)
print()

print("# enumerate() 함수 전용 출력")
print(enumerate(example_list))
print()

print("# list() 함수로 강제 변환 출력")
print(list(enumerate(example_list)))
print()

print("# 반복문 출력")
for i, value in enumerate(example_list):
    print(" {}번째 요소는 {}입니다.".format(i, value))

## reverse(), enumerate()함수는 함수 전용출력이 안된다.