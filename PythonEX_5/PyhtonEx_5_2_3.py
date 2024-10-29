counter = 0
def fibonacci(n):
    print("fibonacci({})를 구합니다.".format(n))
    global counter       # 함수 외부에 있는 변수는 내부에서 참조하지 못하기 때문에 global로 불러옴
    counter += 1
    if n ==1:
        return 1
    if n ==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
fibonacci(10)
print("--------")
print("fibonacci(10) 계산에 쓰인 덧셈 횟수는 {}번입니다.".format(counter))