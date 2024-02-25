def solution(n, k):
    answer = []
    default = int(k)
    while k <= n:
        answer.append(k)
        k += default
        

    return answer