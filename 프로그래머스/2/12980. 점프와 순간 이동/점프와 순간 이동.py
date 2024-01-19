def solution(n):
    count = 1
    while n > 1:
        count += n % 2
        n = n // 2

    return count 