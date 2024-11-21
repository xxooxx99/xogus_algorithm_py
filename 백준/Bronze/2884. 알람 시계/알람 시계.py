H, M = map(int,input().split())

0 <= H <=23

0 <= M <= 59

if M - 45 < 0 :
    if H > 0:
        print(H-1, (60+(M-45)))
    else :
        print(24-(H+1),(60+(M-45)))
elif M - 45 >= 0 :
    print(H, (M-45)) 