from itertools import product
def solution(l, r):
    answer = []
    s1 = len(str(l))
    s2 = len(str(r))
    for s in range(s1, s2+1):
        numbers = list(product('05', repeat=s))
        numbers = [int(''.join(digits)) for digits in numbers if digits[0] != '0']
        for number in numbers:    
            if number >= l and number <= r:
                answer.append(number)
    if not answer:
        answer.append(-1)

    return answer