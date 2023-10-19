# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

def solution(my_str, n):
    answer = []
    my_str = list(my_str)
    for i in range(0, len(my_str), n):
        if i + n < len(my_str):
            answer.append(''.join(my_str[i:i+n]))
        else:
            answer.append(''.join(my_str[i:]))
    return answer

        


# my_str	n	result
# "abc1Addfggg4556b"	6	["abc1Ad", "dfggg4", "556b"]
# "abcdef123"	3	["abc", "def", "123"]





