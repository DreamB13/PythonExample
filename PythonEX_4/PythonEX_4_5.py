# 딕셔너리를 선언
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin": "필리핀"
}

#출력

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
print("ingredient: ", dictionary["ingredient"])
print("origin: ", dictionary["origin"])
print()

#값을 변경
dictionary["name"] = "8D 건조 망고"
print("name: ", dictionary["name"])
dictionary["price"] = 5000   #요소 추가
print(dictionary)
del dictionary["ingredient"] #삭제
print(dictionary)
