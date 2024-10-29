def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

print("1!:", factorial(1))
print("1!:", factorial(2))
print("1!:", factorial(3))
print("1!:", factorial(4))
print("1!:", factorial(5))
print("1!:", factorial(6))

# 자신을 호출 ---------------------------------------
def factorial_recursion(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursion(n-1)
    
print("1!:", factorial(1))
print("2!:", factorial(2))
print("3!:", factorial(3))
print("4!:", factorial(4))
print("5!:", factorial(5))
print("6!:", factorial(6))