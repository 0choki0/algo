# 문자열 my_string이 매개변수로 주어집니다. my_string을 거꾸로 뒤집은 문자열을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    a = list(my_string)
    reversed(a)
    answer = ''.join(a)

    return answer

# my_string	return
# "jaron"	"noraj"
# "bread"	"daerb"