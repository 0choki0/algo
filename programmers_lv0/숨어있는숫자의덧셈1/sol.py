# 문자열 my_string이 매개변수로 주어집니다. 
# my_string안의 모든 자연수들의 합을 return하도록 
# solution 함수를 완성해주세요.

import re

def solution(my_string):
    
    numbers = re.findall(r'\d+', my_string)
    num = ''.join(numbers)
    answer = sum(list(map(int, num)))
    return answer

a = 'aAb1B2cC34oOp'
b = '1a2b3c4d123'

print(solution(a))
print(solution(a))


###########################################

# def solution(my_string):
    
#     for char in my_string:
#         if char.isdigit(): #숫자만 추출하는 함수
#         answer += int(char)

#     return answer


###########################################

def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)
        except: 
            continue
    
    return answer