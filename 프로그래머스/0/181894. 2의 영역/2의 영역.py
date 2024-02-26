def solution(arr):
    for i in range(len(arr)):
        if arr[i] == 2:
            f = i
            break
    for j in range(len(arr)-1, -1 ,-1):
        if arr[j] == 2:
            e = j
            break
    
    if 'f' not in locals():
        return [-1]
    elif f == e:
        return [2]
    else:
        return arr[f:e+1]