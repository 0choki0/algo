def div(num):
    div_list = {}
    div_n = 2
    while num != 1:
        if num % div_n == 0:
            if div_n not in div_list.keys():
                div_list[div_n] = 0
            div_list[div_n] += 1
            num = num / div_n
        else:
            div_n += 1
    return div_list

def solution(arr):
    lcm = {}
    for i in arr:
        for key, value in div(i).items():
            if key not in lcm.keys():
                lcm[key] = 0
            if value >= lcm[key]:
                lcm[key] = value
    
    answer = 1
    for key, value in lcm.items():
        answer *= (key) ** value
    return answer
