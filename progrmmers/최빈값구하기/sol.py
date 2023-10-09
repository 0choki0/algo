# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
# 정수 배열 array가 매개변수로 주어질 때, 
# 최빈값을 return 하도록 solution 함수를 완성해보세요. 
# 최빈값이 여러 개면 -1을 return 합니다.

a = [1, 2, 3, 3, 3, 4]
b = [1, 1, 2, 2]
c = [1,2,3]

def solution(array):

    my_list = list(set(array)) 
    my_mode = [] 
    for num in my_list: 
        n = 0 
        for i in array: 
            if i == num: 
                n += 1 
        my_mode.append(n) 

    my_dict = dict(zip(my_list, my_mode)) 
    
    case2 = sorted(my_mode) 

    if len(my_list) == 1: 
        answer = array[0]
    elif case2[-1] == case2[-2]: 
        answer = -1
    else:
        answer = max(my_dict, key=my_dict.get) 

    return answer

print(solution(a))
print(solution(b))
print(solution(c))

