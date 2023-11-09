# 문자열 my_string이 매개변수로 주어질 때, my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 return 하도록 solution 함수를 작성해보세요.

def solution(my_string):
    answer = []
    for i in my_string:
        if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
            answer.append(i)
    
    return list(map(int, sorted(list(answer))))


# my_string	result
# "hi12392"	[1, 2, 2, 3, 9]
# "p2o4i8gj2"	[2, 2, 4, 8]
# "abcde0"	[0]

print(solution('hi12392'))