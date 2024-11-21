def solution(video_len, pos, op_start, op_end, commands):
    # 시간 문자열을 초로 변환하는 함수
    def time_to_seconds(time_str):
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    
    # 초를 "mm:ss" 형식으로 변환하는 함수
    def seconds_to_time(seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes:02d}:{secs:02d}"
    
    # 초기 설정
    video_length = time_to_seconds(video_len)
    current_pos = time_to_seconds(pos)
    opening_start = time_to_seconds(op_start)
    opening_end = time_to_seconds(op_end)
    
    # 초기 위치가 오프닝 구간에 있는지 확인하고, 건너뛰기
    if opening_start <= current_pos <= opening_end:
        current_pos = opening_end
    
    for command in commands:
        if command == "prev":
            current_pos -= 10
            if current_pos < 0:
                current_pos = 0
        elif command == "next":
            current_pos += 10
            if current_pos > video_length:
                current_pos = video_length
        
        # 명령을 처리한 후, 현재 위치가 오프닝 구간에 있는지 확인하고, 건너뛰기
        if opening_start <= current_pos <= opening_end:
            current_pos = opening_end
    
    return seconds_to_time(current_pos)
