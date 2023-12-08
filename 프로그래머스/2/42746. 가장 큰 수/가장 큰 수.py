def solution(numbers):
    numbers = list(map(str, numbers))
    length = list()
    for num in numbers:
        length.append(len(num))
    lm = max(length)
    numbers.sort(key=lambda x: x*(lm//len(x)+1), reverse=True)
    answer = ''.join(numbers)
    return answer if int(answer) else '0'