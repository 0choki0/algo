# 두 배열이 얼마나 유사한지 확인해보려고 합니다. 문자열 배열 s1과 s2가 주어질 때 같은 원소의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer

# s1	s2	result
# ["a", "b", "c"]	["com", "b", "d", "p", "c"]	2
# ["n", "omg"]	["m", "dot"]	0