import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    numbers = input()

    # 숫자별로 몇 개인지 세기 
    counter = [0 for i in range(10)]
    for number in numbers:
        counter[int(number)] += 1
    
    # 숫자 찾기
    idx = 0
    is_babygin = 0

    while idx < len(counter):
        # 같은 수가 3개 이상인 숫자 찾기
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1
        
        # 3개의 숫자가 연달아 나오는 조합 찾기
        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]:
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
        
        idx += 1
    
    if is_babygin == 2:
        print(True)
    else:
        print(False)

            
    

