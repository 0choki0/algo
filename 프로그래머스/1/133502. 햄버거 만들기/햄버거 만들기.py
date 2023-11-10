def solution(ingredient):
    ingredient = ''.join(map(str, ingredient))
    hamberger = ''
    answer = 0
    for i in ingredient:
        hamberger += i
        if hamberger[-4:] == '1231':
            hamberger = hamberger[:-4]
            answer += 1
    return answer