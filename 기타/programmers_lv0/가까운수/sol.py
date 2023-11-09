# 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

def solution(array, n):
    new = []
    for i in range(len(array)):
        new.append(abs(array[i] - n))

    if new.count(min(new)) == 1:
        return array[new.index(min(new))]

    else:
        a1 = array[new.index(min(new))]
        del array[new.index(min(new))]
        new.remove(min(new))
        a2 = array[new.index(min(new))]

        if a1 < a2:
            return a1
        else:
            return a2

# array	n	result
# [3, 10, 28]	20	28
# [10, 11, 12]	13	12

print(solution([10, 12, 13], 11))