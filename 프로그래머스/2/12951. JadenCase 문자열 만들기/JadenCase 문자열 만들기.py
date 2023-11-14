def solution(s):
    s = s.split(' ')
    answer = []
    for i in s:
        if i != '':
            answer.append(i[0].upper() + i[1:].lower())
        else:
            answer.append('')
        answer.append(' ')
    answer.pop()
    return ''.join(answer)