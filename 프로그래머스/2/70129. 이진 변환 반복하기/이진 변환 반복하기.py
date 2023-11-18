def solution(s):
    times = 0
    count0 = 0

    while s != '1':
        count0 += s.count('0')
        s = s.replace('0', '')
        s = str(bin(int(len(s))))[2:]
        times += 1

    answer = [times, count0]
    return answer