def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3,"Hello", "my", "world")

# ****가변 매개변수 타입이 튜플이다.****