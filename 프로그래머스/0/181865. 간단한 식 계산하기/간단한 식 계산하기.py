def solution(binomial):
        
    if '+' in binomial:
        num = binomial.split('+')
        a = int(num[0])
        b = int(num[1])
        return a + b
    
    elif '-' in binomial:
        num = binomial.split('-')
        a = int(num[0])
        b = int(num[1])
        return a - b
    
    else:
        num = binomial.split('*')
        a = int(num[0])
        b = int(num[1])
        return a*b
    