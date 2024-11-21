def RESTRICTION(N, M):
    if (1 <= N <= 100) and (1 <= M <= 100):
        return False
    return True

def main():
    # N과 M 입력받기
    N, M = map(int, input().split())

    # N, M 제한 조건 확인
    if RESTRICTION(N, M):
        raise ValueError("Restriction Error")

    # N개의 바구니 초기화
    baskets = [0] * N

    # M만큼 추가 입력 받기
    for _ in range(M):
        A, B, C = map(int, input().split())
        for i in range(A - 1, B):
            baskets[i] = C

    # 결과 출력
    print(" ".join(map(str, baskets)))

if __name__ == "__main__":
    main()
