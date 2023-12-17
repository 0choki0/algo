def solution(name):

    if set(name) == {'A'}:
        return 0

    a_pos = ord('A') 
    z_pos = ord('Z')

    answer = float('inf')

    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i] 
        r_l = name[i: :-1] + name[i+1:][::-1] 
        for n in [l_r,r_l]:

            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c)-a_pos, (z_pos+1) - ord(c)) for c in n ]
            answer = min(answer, i + (len(cnt)-1) + sum(cnt))

    return answer



# def target(n):
#     start = n
#     end = 1 + 25 - n
#     return min([start, end])

# def special(A):
#     count = 0
#     max_len = 0
#     for i in A:
#         if i == 'A':
#             count += 1
#             max_len = max([count, max_len])
#         else:
#             count = 0
#     return max_len
    
# def solution(name):
#     alpha = { key:value for value, key in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}

#     count = 0
#     for i in name:
#         count += target(alpha[i])

#     if 'A' not in name:
#         temp = len(name) - 1
#     else:
#         A = 'A'*special(name)
#         name = name.replace(A,'/')
#         name = name.split('/')
#         if len(name[0]) == 0 and len(name[1]) == 0:
#             temp = 0
#         elif len(name[0]) == 0:
#             temp = len(name[1])
#         elif len(name[1]) == 0:
#             temp = len(name[0]) - 1
#         else:
#             temp = min([(len(name[0])-1)*2 + len(name[1]),]) 

#     return count + temp

# print(solution('BBBBAAAABA'))

