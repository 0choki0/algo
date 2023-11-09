# 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

# n 이하에서 소수 찾아서 전체 갯수에서 빼기 3, 4, 5, 6

def solution(n):
    if n == 1:
        return 0
    else:
        answer = n - 2
        for i in range(1, n+1, 2):
            t = 0
            for j in range(1, i+1):
                if i % j == 0:
                    t += 1
            if t == 2:
                answer -= 1

        return answer
    

# # n	result
# # 10	5
# # 15	8

print(solution(10))
print(solution(15))