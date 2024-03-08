def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        new_arr = arr[s:e+1]
        temp_list = []
        for n in new_arr:
            if n > k:
                temp_list.append(n)
        if not temp_list:
            answer.append(-1)
        else:
            answer.append(min(temp_list))
    return answer