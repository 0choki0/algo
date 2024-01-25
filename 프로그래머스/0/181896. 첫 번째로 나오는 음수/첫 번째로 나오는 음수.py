def solution(num_list):
    answer = 0
    for num in num_list:
        if num < 0:
            return answer
        else:
            answer+= 1
    answer = -1
    return answer