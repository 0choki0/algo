def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
def solution(n, k):
    answer = list()
    number_list = list()
    for i in range(1, n+1):
        number_list.append(i)
    
    def step(number_list, k):
        quo, remain = divmod(k, factorial(len(number_list)-1))
        if remain == 0:
            answer.append(number_list[quo-1])
            del number_list[quo-1]
            return answer + number_list[::-1]
        else:
            answer.append(number_list[quo])
            del number_list[quo]
            return step(number_list, remain)
    
    return step(number_list, k)