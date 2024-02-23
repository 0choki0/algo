def solution(n, k):
    num = ''
    while n != 0:
        num += str(n % k)
        n = n//k

    num = num[::-1]
    num = num.split('0')
    while '' in num:
        num.remove('')
    answer = 0
    for n in num:
        if n == '1':
            continue
        temp = int(int(n)**(1/2))+1
        while temp > 2:
            if int(n) % temp == 0:
                break
            else:
                temp -= 1
        if temp == 2:
            answer += 1
            print(n)
    return answer