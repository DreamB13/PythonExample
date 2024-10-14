base = float(input("밑변의 길이를 입력해주세요: "))
height = float(input("높이의 길이를 입력해주세요: "))

hypotenuse = ((base**2)+(height**2))**0.5
print("빗변의 길이는 {}입니다.".format(hypotenuse))