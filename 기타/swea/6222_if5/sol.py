# 다음의 결과와 같이 입력된 문자가 대문자일 경우 소문자로, 
# 소문자일 경우 대문자로 변경하고,
# 알파벳이 아닐 경우엔 그냥 출력하는 코드를 작성하십시오.
# 출력 시 아스키코드를 함께 출력합니다.

import sys
sys.stdin = open('input.txt')

char = input()
#알파벳 검증
if char.isalpha():
    #소문자인 경우
    if char.islower():
        result = char.upper()
    #대문자인 경우
    else:
        result = cahr.lower()
    print(f'{char}(ASCII: {ord(char)}) => {result}(ASCII: {ord(result)})')
else:
    print(char)