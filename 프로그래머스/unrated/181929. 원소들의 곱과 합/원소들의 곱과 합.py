def solution(num_list):
    a = 1
    for i in num_list:
        a *= i
    b = sum(num_list) ** 2
    return 0 if a > b else 1