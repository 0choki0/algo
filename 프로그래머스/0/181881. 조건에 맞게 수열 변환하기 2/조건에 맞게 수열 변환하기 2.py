def solution(arr):
    # 원소 하나를 반복하여 변하지 않는 최대 지점이 되는 횟수를 answer 배열에 저장
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            temp = i / 2
        elif i < 50 and i % 2 == 1:
            temp = i * 2 + 1
        else:
            temp = int(i)
        
        count = 0 
        while i != temp:
            i = int(temp)

            if temp >= 50 and temp % 2 == 0:
                temp = temp / 2
            elif temp < 50 and temp % 2 == 1:
                temp = temp * 2 + 1

            count += 1
        answer.append(count)
    
    return max(answer)