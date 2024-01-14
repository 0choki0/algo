def solution(elements):
    amounts = len(elements)
    elements += elements
    answer = []
    for i in range(1, amounts+1):
        for j in range(amounts):
            answer.append(sum(elements[j:j+i]))
    result = len(set(answer))

    return result