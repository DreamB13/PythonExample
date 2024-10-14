dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin": "필리핀"
}

#존재하지 않는 키에 접근      get()은 dictionary[key]랑 같은 기능이지만 없는 키는 None값을 보냄
value = dictionary.get("존재하지 않는 키")
print("값: ",value)

if value == None:
    print("존재하지 않는 키 접근")