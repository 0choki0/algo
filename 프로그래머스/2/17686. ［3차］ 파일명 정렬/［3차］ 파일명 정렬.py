def solution(files):
    my_list = list()
    for n, file in enumerate(files):
        div = list()
        for i, f in enumerate(file):
            if f.isdigit():
                div.append(i)
            if not f.isdigit() and div:
                div.append(i)
                break
        if div[-1] == len(file)-1:
            div.append(div[-1]+1)
            
        head = file[:min(div)]
        number = file[min(div):max(div)]
        tail = file[max(div):]
        my_list.append([head, number, tail])
        print([head, number, tail])

    answer = sorted(my_list, key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(ans) for ans in answer]