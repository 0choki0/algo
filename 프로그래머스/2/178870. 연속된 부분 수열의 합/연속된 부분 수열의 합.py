def solution(sequence, k):
    s = 0
    se = [0, 0]
    answer = []
    for i in range(len(sequence)-1, -1, -1):
        s += sequence[i]
        if i == len(sequence) - 1:
            se = [i, i]
        else:
            se[0] = i

        if s == k:
            answer.append(list(se))
            s -= sequence[se[1]]
            se[1] -= 1
        elif s < k:
            continue
        else:
            s -= sequence[se[1]]
            se[1] -= 1
    
    if len(answer) == 1:
        return answer[0]
    else:
        for i in range(len(answer)-1):
            result = answer[i][1] - answer[i][0]
            if result < answer[i+1][1] - answer[i+1][0]:
                return answer[i]
        return [0, result]

print(solution([1, 2, 3, 4, 5],	7))