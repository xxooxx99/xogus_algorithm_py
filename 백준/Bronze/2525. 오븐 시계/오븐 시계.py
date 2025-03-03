A,B = map(int,input().split())
C = int(input())
0 <= A <= 23
0 <= B <= 59
0 <= C <= 1000

D = (B + C)

if D // 60 == 0:
    print(A,D)

elif D // 60 >= 1:
    if (A+(D//60)) > 23: 
        N = ((A+(D//60)) // 24)
        print((A+(D//60))- (24 * N), (D - 60*(D//60)))
    elif (A+(D//60)) <= 23:
        print(A+(D//60), (D - 60*(D//60)))