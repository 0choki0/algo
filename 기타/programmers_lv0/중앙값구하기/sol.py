# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 
# 가장 중앙에 위치하는 값을 의미합니다. 
# 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 
# 정수 배열 array가 매개변수로 주어질 때, 
# 중앙값을 return 하도록 solution 함수를 완성해보세요.

a = [1, 2, 7, 10 ,11]
b = [9, -1 ,0]

def solution(array):
    array = sorted(array)
    answer = array[(len(array) // 2)]
    return answer

print(solution(a))
print(solution(b))