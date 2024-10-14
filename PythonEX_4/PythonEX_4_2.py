list_a = [1,2,3]

print("# 리스트 뒤에 요소 추가 -> append()")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

print("# 리스트 중간에 요소 추가 -> insert()")
list_a.insert(0,10)
list_a.insert(7,6)
print(list_a)

list_b = [1,2,3]

print("# 여러 요소를 한번에 추가 -> extend()")
list_b.extend([4,5,6])
print(list_b)