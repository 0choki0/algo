# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    num = ''
    my_string += '='
    for i in range(0, len(my_string) - 1):
        if my_string[i].isdigit() == True:
            num += my_string[i]
            if my_string[i+1].isdigit() != True:
                num += '+'
    
    if num == '':
        return 0
    else:
        return eval(num.rstrip('+'))
    


# my_string	result
# "aAb1B2cC34oOp"	37
# "1a2b3c4d123Z"	133

print(solution("asdflkj"))