a1, a0 = map(int,input().split())
c = int(input()) 
n0 = int(input()) 
if (a1*n0+a0)<=(c*n0) and (a1 <= c):  #0 ≤ |ai| ≤ 100 이므로 음수일 경우도 고려해야한다.
    print(1)
else:
    print(0)

# f(n) = a1 n + a0 에 대하여 
# f(n) <= c*g(n)인 양의 상수가 존재