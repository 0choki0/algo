def solution(q, r, code):
    answer = ''
    location = 0
    while location != len(code):
        if location % q == r:
            answer += code[location]
        location += 1
    return answer