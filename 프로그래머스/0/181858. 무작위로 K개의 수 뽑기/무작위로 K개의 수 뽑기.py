def solution(arr, k):
    my_dict = {}
    answer = []
    for i in arr:
        if k != 0:
            if i not in my_dict.keys():
                answer.append(i)
                my_dict[i] = 0
                k -= 1
        else:
            return answer
    
    while k != 0:
        answer.append(-1)
        k -= 1

    return answer