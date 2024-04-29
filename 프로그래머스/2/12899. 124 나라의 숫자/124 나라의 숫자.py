def solution(n):
    answer = ''
    t = 1
    m = int(n)
    while True:
        m -= 3**t
        if m <= 0:
            break
        t += 1
    while t != 0:
        c = 3**(t-1)
        a = (c - 1) // 2
        b = 0
        while True:
            n -= c
            if n < a:
                n += c
                break
            b += 1
        if b == 3:
            answer += '4'
        else:
            answer += str(b)

        t -= 1

    return answer