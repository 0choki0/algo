import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    line = list(input())
    stack = []
    for i in range(1, len(line)+1):
        stack.append(line[-i])
        if len(stack) > 1:
            if stack[-1] == stack [-2]:
                stack.pop()
                stack.pop()
        else:
            pass
    print(f'#{tc} {len(stack)}')
   


