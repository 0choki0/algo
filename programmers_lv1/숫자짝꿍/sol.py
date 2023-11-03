# 문제 설명
# 두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

# 예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
# 두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
# X, Y는 0으로 시작하지 않습니다.
# X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.
# 입출력 예
# X	Y	result
# "100"	"2345"	"-1"
# "100"	"203045"	"0"
# "100"	"123450"	"10"
# "12321"	"42531"	"321"
# "5525"	"1255"	"552"

# def solution(X, Y):
#     couple = []
#     Y = list(Y)
#     for i in X:
#         if i in Y:
#             couple.append(i)
#             Y.remove(i)
#     if len(couple) == 0:
#         return '-1'
#     else:
#         couple.sort(reverse=True)
#         if couple[0] =='0':
#             return '0'
#         else:
#             return ''.join(couple)

# def solution(X, Y):
#     num_dict1 = dict(zip([i for i in range(10)], [0 for i in range(10)]))
#     num_dict2 = dict(zip([i for i in range(10)], [0 for i in range(10)]))
#     num_dict = dict(zip([i for i in range(10)], [0 for i in range(10)]))

#     for i in X:
#         num_dict1[int(i)] += 1
#     for i in Y:
#         num_dict2[int(i)] += 1

    
#     for i in range(10):
#         while num_dict1[i] != 0 and num_dict2[i] != 0:
#             num_dict[i] += 1
#             num_dict1[i] -= 1
#             num_dict1[i] -= 1
#     print(num_dict)
    
#     # answer = ''
#     # for i in range(1, 11):
#     #     if num_dict[10-i] != 0:
#     #         answer += str(10-i)*num_dict[-i] 
#     return 

def solution(X, Y):
    answer = ''
    X_list = [0 for i in range(10)]
    Y_list = [0 for i in range(10)]

    for i in X:
        X_list[int(i)] += 1
    for i in Y:
        Y_list[int(i)] += 1
    for i in range(1, 11):
        for j in range(min(X_list[-i], Y_list[-i])):
            answer += str(10-i)
    if len(answer) == 0:
        answer = '-1'
    elif answer[0] == '0':
        answer = '0'
    return answer


print(solution("9977665008","979840015"))