def solution(survey, choices):
    # 각 유형마다 점수를 주기 위해 dictionary 생성 
    char = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0,}
    
    # 점수 부여
    for i in range(len(choices)):
        # 비동의, 모르겠음의 경우
        if choices[i] <= 4:
            # 부여하는 점수
            score = 4-choices[i]
            # survey의 앞 유형
            char[survey[i][0]] += score
        # 동의의 경우
        else:
            # 부여하는 점수
            score = choices[i]-4
            # survey의 뒷 유형
            char[survey[i][1]] += score
    
    # 점수를 기준으로 각각의 유형 판별
    # dict는 순서가 없기에 순서 역할을 할 key를 만들어줌
    new_char = {}
    for i, (key, value) in enumerate(char.items()):
        new_char[i] = (key, value)
    
    answer = ''
    for i in range(0, len(char.keys()), 2):
        if new_char[i][1] >= new_char[i+1][1]:
            answer += new_char[i][0]
        else:
            answer += new_char[i+1][0]
    return answer