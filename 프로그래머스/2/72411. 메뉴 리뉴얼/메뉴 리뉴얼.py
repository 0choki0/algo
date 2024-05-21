import itertools
def solution(orders, course):
    answer = list()
    for n in course:
        comb_dict = dict()
        for order in orders:
            order = ''.join(sorted(order))
            combination = list(itertools.combinations(order, n))
            for comb in combination:
                comb = ''.join(comb)
                if comb not in comb_dict.keys():
                    comb_dict[comb] = 1
                else:
                    comb_dict[comb] += 1
        
        if comb_dict:
            max_order_counted = max(comb_dict.values())
            if max_order_counted >= 2:
                for k, v in comb_dict.items():
                    if v == max_order_counted:
                        answer.append(k)

    return sorted(answer)