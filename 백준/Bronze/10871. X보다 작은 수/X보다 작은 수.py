N,X = map(int,input().split())
if N < 1 or N > 10000 or X < 0 or X > 10000:
    print("unvaluable")
else:
    A = input().split()[:N]
    A = list(map(int,A))
    B = []

for num_list in A:
    if num_list < X:
        B.append(num_list)
print(*B)