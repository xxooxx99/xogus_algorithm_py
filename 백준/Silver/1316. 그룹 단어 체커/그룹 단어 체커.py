def separate(word):
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+2:]:
                return False
    return True

N = int(input())
if N>100:
    print("input error")

data = []
for i in range(N):
    word = str(input())
    data.append(word)

count = 0
for word in data:
    if separate(word):
        count += 1

print(count)