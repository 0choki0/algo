def solution(arr):
    temp = 1
    while temp < len(arr):
        temp *= 2
    arr += [0]*(temp-len(arr))
    return arr