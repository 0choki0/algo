def solution(my_string):
    my_dict = {}
    temp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in temp:
        my_dict[i] = 0
    
    for i in my_string:
        my_dict[i] += 1
    
    return list(my_dict.values())