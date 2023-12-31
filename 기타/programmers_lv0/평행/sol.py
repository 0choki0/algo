# 점 네 개의 좌표를 담은 이차원 배열  dots가 다음과 같이 매개변수로 주어집니다.

# [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]
# 주어진 네 개의 점을 두 개씩 이었을 때, 두 직선이 평행이 되는 경우가 있으면 1을 없으면 0을 return 하도록 solution 함수를 완성해보세요.

def lean(a, b):
    return (b[0]-a[0])/(b[1]-a[1])

def solution(dots):
    if lean(dots[0], dots[1]) == lean(dots[2], dots[3]):
        return 1
    elif lean(dots[0], dots[2]) == lean(dots[1], dots[3]):
        return 1
    elif lean(dots[0], dots[3]) == lean(dots[1], dots[2]):
        return 1
    elif lean(dots[1], dots[2]) == lean(dots[0], dots[3]):
        return 1
    elif lean(dots[1], dots[3]) == lean(dots[0], dots[2]):
        return 1
    elif lean(dots[2], dots[3]) == lean(dots[0], dots[1]):
        return 1
    else:
        return 0

# dots	result
# [[1, 4], [9, 2], [3, 8], [11, 6]]	1
# [[3, 5], [4, 1], [2, 4], [5, 10]]	0


print(solution([[3, 5], [4, 1], [2, 4], [5, 10]]))

