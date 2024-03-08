def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        r = i // n
        c = i % n
        temp = max(r, c) + 1
        answer.append(temp) 

    return answer