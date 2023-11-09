# 문제 설명
# 머쓱이는 태어난 지 11개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음과 네 가지 발음을 
# 조합해서 만들 수 있는 발음밖에 하지 못하고 연속해서 같은 발음을 하는 것을 어려워합니다. 
# 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ babbling의 길이 ≤ 100
# 1 ≤ babbling[i]의 길이 ≤ 30
# 문자열은 알파벳 소문자로만 이루어져 있습니다.
# 입출력 예
# babbling	result
# ["aya", "yee", "u", "maa"]	1
# ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]	2

# def solution(babbling):
#     answer = 0
#     for i in babbling:
#         for j in ['aya','ye','woo','ma']:
#             if j*2 not in i:
#                 i=i.replace(j,' ')
#         if len(i.strip())==0:
#             answer +=1
#     return answer

import itertools

def solution(babbling):
    can = []
    cant = ['ayaaya', 'yeye', 'woowoo', 'mama']

    can1 = ['aya', 'ye', 'woo', 'ma']
    for i in can1:
        can.append(i)

    can2 = list(itertools.product(can1, repeat=2))    
    for i in can2:
        for j in cant:
            if j not in ''.join(list(i)):
                a = 0
            else:
                a = 1
                break
        if a == 0:
            can.append(''.join(list(i)))

    can3 = list(itertools.product(can1, repeat=3))    
    for i in can3:
        for j in cant:
            if j not in ''.join(list(i)):
                a = 0
            else:
                a = 1
                break
        if a == 0:
            can.append(''.join(list(i)))

    can4 = list(itertools.product(can1, repeat=4))    
    for i in can4:
        for j in cant:
            if j not in ''.join(list(i)):
                a = 0
            else:
                a = 1
                break
        if a == 0:
            can.append(''.join(list(i)))



    
    answer = 0
    for i in babbling:
        if i in can:
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
    # can4 = list(itertools.product(can1, repeat=4))    
    # for i in can4:
    #     if ''.join(list(i)) not in cant:
    #         can.append(''.join(list(i)))