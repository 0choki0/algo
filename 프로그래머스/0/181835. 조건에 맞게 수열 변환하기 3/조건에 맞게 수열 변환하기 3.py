def solution(arr, k):
    if k % 2 == 1:
        answer = [k*i for i in arr]
    else:
        answer = [k+i for i in arr]
    return answer