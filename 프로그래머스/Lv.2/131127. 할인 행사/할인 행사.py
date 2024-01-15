def solution(want, number, discount):
    answer = 0

    want_dict = {}
    for key, value in zip(want, number):
        want_dict[key] = value
    
    day = sum(number)

    for i in range(len(discount) - day + 1):
        temp = dict(want_dict)

        for j in discount[i:i+10]:
            if j not in temp.keys():
                continue
            else:
                if temp[j] > 0:
                    temp[j] -= 1
                else:
                    break
        if sum(temp.values()) == 0:
            answer += 1

    return answer