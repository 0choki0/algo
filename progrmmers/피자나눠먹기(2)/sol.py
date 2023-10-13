# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
# n명이 주문한 피자를 남기지 않고 모두 같은 수의 
# 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 
# 하는지를 return 하도록 solution 함수를 완성해보세요.

def solution(n):
    # 6과 n의 최소공배수를 6으로 나눈 몫
    lcm = 1
    answer = 0
    while answer == 0:
        if lcm % 6 == 0 and lcm % n == 0:
            answer = lcm // 6 
            break
        else:
            lcm += 1

    return answer

print(solution(6))
print(solution(4))
print(solution(10))