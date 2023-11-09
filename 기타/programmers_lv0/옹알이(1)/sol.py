# 머쓱이는 태어난 지 6개월 된 조카를 돌보고 있습니다. 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못합니다. 문자열 배열 babbling이 매개변수로 주어질 때, 머쓱이의 조카가 발음할 수 있는 단어의 개수를 return하도록 solution 함수를 완성해주세요.

import itertools

def solution(babbling):
    babbling_list = ["aya", "ye", "woo", "ma"]
    per_list = []
    for i in range(1, len(babbling_list)+1):
        a = list(itertools.permutations(babbling_list, i))
        for j in range(len(a)):
            per_list.append(''.join(a[j]))
    
    answer = 0
    for i in babbling:
        if i in per_list:
            answer += 1
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

# babbling	result
# ["aya", "yee", "u", "maa", "wyeoo"]	1
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]	3



# a = [('가나', '다라'), ('마바', '사아')]
# b = ('마바', '사아')

# print(''.join(a[0]))
