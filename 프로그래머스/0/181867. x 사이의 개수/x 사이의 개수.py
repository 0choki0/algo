def solution(myString):
    answer = []
    count = 0
    for string in myString:
        if string != 'x':
            count += 1
        else:
            answer.append(count)
            count = 0
    answer.append(count)
    return answer