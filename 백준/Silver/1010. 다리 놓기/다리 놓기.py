import sys
input = sys.stdin.readline


def factorial(n):
    f = 1 
    for i in range(n):
        f *= (i+1)
    return f 
    
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m-n)))