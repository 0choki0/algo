def solution(s):
    my_dict = {}
    for i in s[1:-1]:
        if i == '{':
            count = 0
            num = ''
            my_list = []
        elif i.isdigit():
            num += i
        elif i == ',' or i == '}':
            count += 1
            if num != '':
                my_list.append(int(num))
                num = ''
        if i == '}':
            my_dict[count] = my_list
    
    sorted_list = sorted(my_dict.values(), key=len)
    
    answer = []
    for i in sorted_list:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer