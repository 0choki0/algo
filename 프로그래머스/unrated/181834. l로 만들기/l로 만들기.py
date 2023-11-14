def solution(myString):
    alpha = 'abcdefghijk'
    answer = ''
    for i in myString:
        if i in alpha:
            answer += 'l'
        else:
            answer += i
    return answer