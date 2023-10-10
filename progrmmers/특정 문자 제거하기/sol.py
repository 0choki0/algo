# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
# my_string에서 letter를 제거한 문자열을 return하도록 
# solution 함수를 완성해주세요.


def solution(my_string, letter):
    for i1 in my_string:
        for i2 in letter:
            if i1 == i2:
                my_string = my_string.replace(i1, '')
    return my_string

print(solution('abcdef', 'f'))
print(solution('BCBdbe', 'B'))