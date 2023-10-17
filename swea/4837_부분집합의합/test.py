numbers = list(range(1, 5))

n = len(numbers)

for i in range(1<<n): # '1<<n'의 의미는 2진수로 1을 옆으로 n번 밀었다는 것임. 즉 2^n
    print(bin(i))
    temp = []
    for j in range(n):
        # print(i, bin(i), bin(1<<j)) # bin은 2진수로 표현하는 함수
        if i & (1<<j): # i와 j의 (2진수)자릿수가 모두 True 일경우 그 자릿수에 True(1)을 반환
            temp.append(numbers[j])
    print(temp)