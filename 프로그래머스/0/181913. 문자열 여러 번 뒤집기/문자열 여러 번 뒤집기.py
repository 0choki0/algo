def solution(my_string, queries):
    answer = my_string
    for query in queries:
        s = query[0] 
        e = query[1]+1
        temp = answer[s:e][::-1]
        answer = answer[:s] + temp + answer[e:]
    return answer