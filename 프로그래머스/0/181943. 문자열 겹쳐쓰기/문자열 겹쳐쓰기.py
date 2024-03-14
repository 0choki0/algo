def solution(my_string, overwrite_string, s):
    answer = ''
    s2 = len(overwrite_string)
    answer += my_string[:s] + overwrite_string + my_string[s+s2:]
    return answer