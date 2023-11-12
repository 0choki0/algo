def solution(survey, choices):
    char = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0,}
    for i in range(len(choices)):
        if choices[i] <= 4:
            f = 4-choices[i]
            char[survey[i][0]] += f
        else:
            b = choices[i]-4
            char[survey[i][1]] += b

    new_char = {}
    for i, (key, value) in enumerate(char.items()):
        new_char[i] = (key, value)
    
    answer = ''
    for i in range(0, 8, 2):
        if new_char[i][1] >= new_char[i+1][1]:
            answer += new_char[i][0]
        else:
            answer += new_char[i+1][0]
    return answer