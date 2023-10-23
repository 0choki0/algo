# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    numbers.sort()
    if numbers[0]*numbers[1] > numbers[-1]*numbers[-2]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]


# numbers	result
# [1, 2, -3, 4, -5]	15
# [0, -31, 24, 10, 1, 9]	240
# [10, 20, 30, 5, 5, 20, 5]	600

