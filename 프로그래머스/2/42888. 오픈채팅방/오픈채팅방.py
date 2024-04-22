def solution(record):
    state = []
    re_dict = dict()
    for re in record:
        re_list = re.split(sep=' ')
        condition = re_list[0]
        code = re_list[1]
        name = re_list[-1]

        if code not in re_dict.keys():
            re_dict[code] = name
        else:
            if condition != 'Leave':
                re_dict[code] = name

        if condition != 'Change':
            state.append((code, condition))
    
    answer = []
    for s in state:
        name = re_dict[s[0]]
        if s[-1] == 'Enter':
            condition = '들어왔습니다.'
        else:
            condition = '나갔습니다.'
        answer.append(f'{name}님이 {condition}')

    return answer