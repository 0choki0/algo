str = input()
answer = ''
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in str:
    if i in alpha:
        answer += i.upper()
    else:
        answer += i.lower()
print(answer)