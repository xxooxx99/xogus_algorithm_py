def solution():
    answers = set() #중복제거를 위한 집합 사용
    for _ in range(10):
        N = int(input())
        answers.add(N % 42) #나머지를 바로 집합에 추가
    print(len(answers)) #집합의 길이 = 서로 다른 나머지의 갯수

solution()