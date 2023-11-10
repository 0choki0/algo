def solution(a, b):
    r1 = str(a) + str(b)
    r2 = str(b) + str(a)
    if int(r1) >= int(r2):
        return int(r1)
    else:
        return int(r2)