import string

def convert(n, base):
    number = string.digits + string.ascii_uppercase
    q, r = divmod(n, base)

    return convert(q, base) + number[r] if q else number[r]

def solution(n, t, m, p):
    answer = ''
    num = 0
    while len(answer) <= t*m:
        answer += convert(num, n)
        num += 1
    answer = answer[:t*m]

    my_answer = ''
    if m == p:
        p = 0
    for n, i in enumerate(answer,1):
        if n%m == p:
            my_answer += i
        else:
            continue

    return my_answer