#정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(num_list):
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    answer = [a, b]
    return answer


# num_list	result
# [1, 2, 3, 4, 5]	[2, 3]
# [1, 3, 5, 7]	[0, 4]