def solution(str_list):
    answer = []
    for str in str_list:
        if str == 'l':
            return answer 
            break
        elif str == 'r':
            return str_list[len(answer)+1:]
            break
        else:
            answer.append(str)
    return []
