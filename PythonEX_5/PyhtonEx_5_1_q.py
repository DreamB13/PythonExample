def mul(*values):
    value = 1
    for i in values:
        value *= i
    return value
print(mul(5,7,9,10))