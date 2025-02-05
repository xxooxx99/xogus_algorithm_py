    #첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.(N만큼 입력받음)
    # 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 
    # 적어도 하나의 값은 0보다 크다.
    #플로우
    #예외처리-> 입력값 유효성 확인
    #입력값 유효성이 확인되었다면, N input값 받기, 그다음 N만큼 scores를 입력받고, 이를 리스트 형태로 저장
    #리스트중 가장 큰수를 M으로 지정
    #def result_score 함수를 통해 M보다 작은 모든 숫자에 100/M을 곱한다
    #결과 출력

#입력값 유효성 검사
def isvalid(N,scores):
    #N의 범위 확인
    if not(1 <= N <= 1000):
        raise ValueError("N의 입력범위를 벗어났습니다.")
    
    #scores의 개수가 N과 일치하는지 확인
    if len(scores) != N:
        raise ValueError("입력된 점수의 개수가 N과 다릅니다.")

    #각 점수가 0 이상 100이하인지 확인
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("점수의 입력범위를 벗어났습니다.")

    #적어도 하나의 점수가 0보다 큰지 확인
    if not any(score > 0 for score in scores):
        raise ValueError("적어도 하나의 점수는 0보다 커야합니다.")

        
    return True

    


def result_score(scores):
    max_score = max(scores)
    if max_score == 0:
        raise ValueError("최대 점수가 0입니다. 반환할 수 없습니다.")
    return [score * 100 / max_score for score in scores]

def solution():
    try:
        N = int(input().strip())
        scores = list(map(int,input().split()))

        #입력값 검증
        
        isvalid(N, scores)

        #점수 변환
        
        new_scores = result_score(scores)

        avg_score = sum(new_scores) / len(new_scores)
        print(avg_score)
    except Exception as e:
        print("입력값 오류:",e)

if __name__ == "__main__":
    solution()
    