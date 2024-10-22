#next()함수와 reversed()함수: 이터레이터
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers)

print('reversed numbers :', r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))