array = []

for i in range(0,20,2):
    array.append(i*i)

print(array)

# 리스트 안에 for문 사용
array = [i*i for i in range(0,20,2)]
print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit 
          for fruit in array 
          if fruit != "초콜릿"]

print(output)