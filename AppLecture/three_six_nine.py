num = input()
if ('3' in num) or ('6' in num) or ('9' in num):
    three = num.count('3')
    six = num.count('6')
    nine = num.count('9')

    time = three+six+nine
    print('짝'*time)
else:
    print(num)