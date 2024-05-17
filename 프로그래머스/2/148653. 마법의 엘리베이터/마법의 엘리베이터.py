def solution(storey):
    answer = 0
    storey =str(storey)
    while True :
        if len(storey) == 1:
            storey = int(storey)
            if storey <= 5:
                answer += storey
            else:
                answer += 11 - storey
            break

        if storey[-2] in '01234':
            if storey[-1] in '012345':
                answer += int(storey[-1])
                storey = storey[:-1]
            elif storey[-1] in '6789':
                answer += 10 - int(storey[-1])
                storey = str(int(storey[:-1])+1)

        elif storey[-2] in '56789':
            if storey[-1] in '01234':
                answer += int(storey[-1])
                storey = storey[:-1]
            elif storey[-1] in '56789':
                answer += 10 - int(storey[-1])
                storey = str(int(storey[:-1])+1)
        

    return answer 

print(solution(545))
