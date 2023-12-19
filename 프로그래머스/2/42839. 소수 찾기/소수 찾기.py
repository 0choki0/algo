from itertools import permutations

def prime(number):
    for n in range(2, int(number**0.5)+1):
        if number % n == 0:
            return
    return number

def solution(numbers):
    answer = []
    for n in range(1, len(numbers)+1):
        temp = list(permutations(numbers, n))
        for i in temp:
            a = ''
            for j in i:
                a += str(j)
            a = int(a)
            if a != 0 and a != 1 and prime(a) != None:
                answer.append(a)

    return len(set(answer))