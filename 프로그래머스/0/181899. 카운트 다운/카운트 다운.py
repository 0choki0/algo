def solution(start, end_num):
    answer = []
    while start > end_num-1:
        answer.append(start)
        start -= 1
    return answer