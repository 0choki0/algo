def solution(k, tangerine):
    tangerine_size = {}
    for i in tangerine:
        if i not in tangerine_size:
            tangerine_size[i] = 1
        else:
            tangerine_size[i] += 1
    
    box = 0 
    amount = sorted(tangerine_size.values(), reverse=True)
    
    answer = 0
    for i in amount:
        box += i
        answer += 1
        if box >= k:
            break
    
    return answer