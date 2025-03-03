def solve(a):
    return sum(a)

# 함수 테스트
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    print(solve(data))
