def solution(a, b):
    r1 = int(str(a)+str(b))
    r2 = 2 * a * b
    if r1 >= r2:
        return r1
    else:
        return r2