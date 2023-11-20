def solution(s):
    answer = 0
    s = list(s)

    for i in range(len(s)):
        temp = ''.join(s)
        while '[]' in temp or '{}' in temp or '()' in temp:
            temp = temp.replace('[]', '')
            temp = temp.replace('{}', '')
            temp = temp.replace('()', '')
        if len(temp) == 0:
            answer += 1
        
        s.append(s.pop(0))
    
    return answer
        