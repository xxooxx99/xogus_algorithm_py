T = int(input())
for i in range(T):
    result = []
    A,B = input().split(" ")
    C = len(B)
    for j in range(C):
        result += int(A) * (B[j])
    print(''.join(result))
