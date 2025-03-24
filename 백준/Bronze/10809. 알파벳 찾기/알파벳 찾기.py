a = input()

for i in range(26):
    alpha = chr(97 + i)

    if alpha in a:
        print(a.index(alpha), end = ' ')
    else:
        print(-1,end = ' ')