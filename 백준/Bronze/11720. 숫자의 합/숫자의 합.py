a = int(input())
b = input()

if len(b) != a:
    print("올바르지 않은 입력값")
else:
    print(sum(map(int,list(b))))
