def solution(numbers):
    answer = []
    for n in numbers:
        std = '0' + bin(n)[2:]
        for i in range(len(std)-1, -1, -1):
            if i == len(std)-1 and std[i] == '0':
                std = '0b' + std[:i] + '1'
                break
            else:
                if std[i] == '0':
                    std = '0b' + std[:i] + '10' + std[i+2:]
                    break
        answer.append(int(std, 2))
    return answer