def solution(strArr):
    answer = []
    even_odd = 1
    for index in strArr:
        if even_odd == 1:
            answer.append(index.lower())
            even_odd = 2
        else:
            answer.append(index.upper())
            even_odd = 1
        
    return answer