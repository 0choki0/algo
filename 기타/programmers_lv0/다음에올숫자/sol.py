# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 하도록 solution 함수를 완성해보세요.

def solution(common):
    for i in range(len(common)-2):
        if common[i+1] - common[i] == common[i+2] - common[i+1]:
            d = common[i+1] - common[i]
            answer = common[-1] + d
        else:
            answer = common[-1] * (common[1] / common[0]) 

    return answer

# common	result
# [1, 2, 3, 4]	5
# [2, 4, 8]	16

print(solution([1, 2, 3, 4]))
print(solution([2, 4, 8]))
