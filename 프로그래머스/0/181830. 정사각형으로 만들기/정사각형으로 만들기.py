def solution(arr):
    l1 = len(arr[0])
    l2 = len(arr)
    l = max(l1, l2)
    answer = []
    for a in arr:
        while len(a) != l:
            a.append(0)
        answer.append(a)
    
    while len(answer) != l:
        temp = [0]*l 
        answer.append(temp)

    return answer