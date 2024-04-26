def solution(n):
    n1 = 1
    n2 = 2
    k = 3

    if n == 1:
        return n1
    elif n == 2:
        return n2 
    else:
        while True:
            n1, n2 = n2, n1+n2
            if k == n:
                break
            k += 1
        return n2 % 1000000007