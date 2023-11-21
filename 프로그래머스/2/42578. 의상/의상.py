def solution(clothes):
    clothes_dict = {}
    for i in clothes:
        if i[1] not in clothes_dict:
            clothes_dict[i[1]] = [i[0]] 
        else:
            clothes_dict[i[1]].append(i[0])
    
    answer = 1
    for cloth in clothes_dict.values():
        answer *= len(cloth) + 1
        
    
    return answer - 1