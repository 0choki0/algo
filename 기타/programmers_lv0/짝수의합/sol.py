def solution(n):
    l = range(1, n+1)
    b = []
    for even in l:
        if even % 2 == 1:
            pass
        else:
            b.append(even)

    answer = sum(b)
    return answer


print(solution(10))
print(solution(4))