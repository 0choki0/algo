def solution(A, B):
    point = 0
    
    A.sort()
    B.sort()

    a, b = 0, 0
    while a != len(A) and b != len(B):
        if B[b] > A[a]:
            point += 1
            a += 1
            b += 1
        else:
            b += 1

    return point