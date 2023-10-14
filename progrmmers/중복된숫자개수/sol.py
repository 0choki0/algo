# 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer

# array	n	result
# [1, 1, 2, 3, 4, 5]	1	2
# [0, 2, 3, 4]	1	0

a = [1, 1, 2, 3, 4, 5]
b = [0, 2, 3, 4]
print(solution(a, 1))
print(solution(b, 1))