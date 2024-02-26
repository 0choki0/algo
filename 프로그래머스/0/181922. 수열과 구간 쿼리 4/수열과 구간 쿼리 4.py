def solution(arr, queries):
    answer = []
    my_dict = {}
    
    for i in range(len(arr)):
        my_dict[i] = 0
    
    for query in queries:
        for q in range(query[0], query[1]+1):
            if q % query[2] == 0:
                my_dict[q] += 1
        
    for i in range(len(arr)):
        answer.append(arr[i]+my_dict[i])
    
    return answer