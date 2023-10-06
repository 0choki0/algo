def solution(numbers):
    answer = sum(numbers) / len(numbers)
    return answer

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(solution(a))
print(solution(b))