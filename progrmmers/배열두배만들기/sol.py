# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 각 원소에 두배한 원소를 가진 배열을 
# return하도록 solution 함수를 완성해주세요.

a = [1, 2, 3, 4, 5]
b = [1, 2, 100, -99, 1 , 2, 3]
my_list = []

def solution(numbers):
    for i in numbers:
        t = 2 * i
        my_list.append(t)
    
    answer = my_list
    return answer

print(solution(a))
print(solution(b))