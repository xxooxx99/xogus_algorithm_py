a, b, c = map(int,input().split())

if a == b == c:
    print(10000 + (a * 1000))
elif a==b or a==c:
    print(1000 + (a * 100))
elif b==c:
    print(1000 + (b * 100))
elif a != b != c:
    if a < b and c < b:
        print(b * 100)
    elif a < b and c > b:
        print(c*100)
    elif a > b and c < b:
        print(a * 100)
    elif a > b and c > b:
        if a > c:
            print(a*100)
        else:
            print(c * 100)
