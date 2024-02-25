def solution(msg):
    answer = []
    my_dict = {}
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = 1
    for i in alpha:
        my_dict[i] = number
        number += 1

    while msg:
        for i in range(len(msg)):
            if msg[:i+1] in my_dict.keys():
                continue
            else:
                my_dict[msg[:i+1]] = number
                number += 1
                answer.append(my_dict[msg[:i]])
                msg = msg[i:]
                break
        
        if msg in my_dict.keys():
            answer.append(my_dict[msg])
            msg = ''

    return answer