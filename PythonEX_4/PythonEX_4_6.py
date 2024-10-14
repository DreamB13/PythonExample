dictionary = {
    "name": "망고",
    "type": "당절임",
    "ingredient": ["망고","설탕","메타중아황산나트륨","치자황색소"],
    "origin": "필리핀"
}

#사용자가 키 입력하기
key = input("접근하려는 키: ")

#출력
if key in dictionary:
    print(dictionary[key])
else:
    print("잘못된 키입니다.")