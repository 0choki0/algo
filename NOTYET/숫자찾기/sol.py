# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

def solution(num, k):
    for i in list(str(num)):
        if i == str(k):
            return num.index(int(i)) + 1
        else:
            return -1 




# num	k	result
# 29183	1	3
# 232443	4	4
# 123456	7	-1

print(solution(29183, 1))
# print(solution(232443, 4))
# print(solution(123456, 7))





