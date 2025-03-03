N =int(input())
if N< -1000000 or  N > 1000000:
    print("unvalue")
else:
    A = input().split()[:N]
    A = list(map(int,A))

print(min(A),max(A))