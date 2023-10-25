# 한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

def solution(polynomial):
    polynomial = polynomial.split()
    x = 0
    num = 0
    for i in polynomial:
        if 'x' in i:
            if i == 'x':
                x += 1
            else:
                x += int(i.replace('x', ''))
        elif i == '+':
            pass
        else:
            num += int(i)


    if num == 0:
        if x == 1:
            return f'x'
        else:
            return f'{x}x'
    elif x == 0:
        return f'{num}'
    else:
        if x == 1:
            return f'x + {num}'
        else:
            return f'{x}x + {num}'
    

# polynomial	result
# "3x + 7 + x"	"4x + 7"
# "x + x + x"	"3x"



print(solution("11 + 14x + 4 + x"))
