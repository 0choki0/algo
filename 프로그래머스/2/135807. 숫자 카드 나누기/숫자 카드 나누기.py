from math import gcd

def solution(arrayA, arrayB):
    arrayA, arrayB = list(set(arrayA)), list(set(arrayB))
    answer = [0]

    def GCD(array):
        for i, a in enumerate(array):
            if i == 0:
                g = gcd(False,a)
            else:
                g = gcd(g, a)
        return g
    
    def N_GCD(array, GCD):
        for i, a in enumerate(array):
            if a % GCD == 0:
                return 0
        return GCD
    
    answer.append(N_GCD(arrayA, GCD(arrayB)))
    answer.append(N_GCD(arrayB, GCD(arrayA)))
    
    return max(answer)