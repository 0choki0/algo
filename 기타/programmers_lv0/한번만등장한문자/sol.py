# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

def solution(s):
    s = sorted(list(s))
    a = []
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            a.append(s[i])
    return ''.join(sorted(list(set(s) - set(a))))


# s	result
# "abcabcadc"	"d"
# "abdc"	"abcd"
# "hello"	"eho"
print(solution('hello'))