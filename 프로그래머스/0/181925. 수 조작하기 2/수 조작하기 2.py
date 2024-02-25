def solution(numLog):
    answer = ''
    temp = 0
    for num in numLog:
        temp = num - temp
        if temp == 1:
            answer += 'w'
        elif temp == -1:
            answer += 's'
        elif temp == 10:
            answer += 'd'
        else:
            answer += 'a'
        temp = num

        
    return answer[1:]