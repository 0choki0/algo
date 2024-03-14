def solution(code):
    answer = ''
    mode = 0
    mode2 = 1
    count = 0
    for i in code:
        if i == '1':
            mode, mode2 = mode2, mode
            count += 1
            continue
        if mode == 0:
            if count % 2 == 0:
                answer += i
        else:
            if count % 2 == 1:
                answer += i
        count += 1
    
    if not answer:
        answer += "EMPTY"
    return answer