def solution(weights):
    answer = 0
    weight_dict = dict()
    possible = [2/4, 3/4, 2/3, 4/3, 3/2, 4/2]
    
    for weight in weights:
        if weight not in weight_dict.keys():
            weight_dict[weight] = 1
        else:
            weight_dict[weight] += 1
    
    temp = 0
    for k, v in weight_dict.items():
        for poss in possible:
            p = poss*k
            if p in weight_dict.keys():
                answer += v*(weight_dict[p])
        if v >= 2:
            temp += v*(v-1)/2
            

    return answer/2 + temp