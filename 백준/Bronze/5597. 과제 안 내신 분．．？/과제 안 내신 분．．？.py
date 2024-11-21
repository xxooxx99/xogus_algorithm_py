def main():
    #학생 출석번호 초기화
    all_students = set(range(1,31))

    #28명의 출석번호 입력받기
    for _ in range(28):
        n = int(input())
        if 1 <= n <= 30:
            all_students.remove(n)

    #출석하지 않은 학생 출력
    missing_students = sorted(all_students)
    for student in missing_students:
        print(student)

if __name__== "__main__" :
    main()

