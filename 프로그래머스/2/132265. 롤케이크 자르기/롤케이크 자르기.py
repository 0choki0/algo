def solution(topping):
    answer = 0
    back = dict()
    for t in topping:
        if t in back:
            back[t] += 1
        else:
            back[t] = 1
    
    front = dict()
    for t in topping:
        if len(front) == len(back):
            answer += 1
        if t not in front:
            front[t] = 1
        back[t] -= 1
        if back[t] == 0:
            del back[t]
    return answer
