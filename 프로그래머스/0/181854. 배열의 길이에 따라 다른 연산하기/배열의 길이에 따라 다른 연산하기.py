def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        eo = 1
        for i in arr:
            if eo == 1:
                answer.append(i)
                eo = 2
            else:
                answer.append(i+n)
                eo = 1
                
    else:
        eo = 1
        for i in arr:
            if eo == 1:
                answer.append(i+n)
                eo = 2
            else:
                answer.append(i)
                eo = 1
    return answer