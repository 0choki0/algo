def solution(strArr):
    my_dict = {}
    for s in strArr:
        if len(s) in my_dict.keys():
            my_dict[len(s)] += 1
        else:
            my_dict[len(s)] = 1
    
    arr = my_dict.values()
    answer = max(arr)
    return answer