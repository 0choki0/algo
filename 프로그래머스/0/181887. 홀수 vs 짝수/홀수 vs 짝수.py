def solution(num_list):
    eo = 1
    odd = 0
    even = 0
    for i in num_list:
        if eo == 1:
            odd += i
            eo = 2
        else:
            even += i
            eo = 1
        
    return max(odd, even)