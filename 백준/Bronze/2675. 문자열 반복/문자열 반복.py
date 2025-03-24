T = int(input())
for i in range(T):
    result = []
    A,B = input().split(" ")
    C = len(B)
    for i in range(C):
        result += int(A) * (B[i])
    print(''.join(result))
