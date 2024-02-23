def solution(str1, str2):
    str1_list = []
    str2_list = []
    
    temp = ''
    for i in str1:
        temp += i
        if len(temp) > 2:
            temp = temp[1:]
        if len(temp) == 2 and temp.isalpha():
            str1_list.append(temp.upper())

    temp = ''
    for i in str2:
        temp += i
        if len(temp) > 2:
            temp = temp[1:]
        if len(temp) == 2 and temp.isalpha():
            str2_list.append(temp.upper())

    numerator = 0
    for i in str1_list:
        if i in str2_list:
            numerator += 1
            str2_list.remove(i)

    denominator = len(str1_list) + len(str2_list)

    if denominator == 0:
        return 65536


    return int(numerator / denominator * 65536) 