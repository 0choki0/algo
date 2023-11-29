def how_sort(data, sort_by):
    if sort_by == 'code':
        return sorted(data, key=lambda x:x[0])
    elif sort_by == 'date':
        return sorted(data, key=lambda x:x[1])
    elif sort_by == 'maximum':
        return sorted(data, key=lambda x:x[2])
    elif sort_by == 'remain':
        return sorted(data, key=lambda x:x[3])


def solution(data, ext, val_ext, sort_by):
    
    new_data = []

    if ext == 'code':
        for code in data:
            if code[0] <= val_ext:
                new_data.append(code)
    
    elif ext == 'date':
        for date in data:
            if date[1] <= val_ext:
                new_data.append(date)
    
    elif ext == 'maximum':
        for maximum in data:
            if maximum[2] <= val_ext:
                new_data.append(maximum)
    
    elif ext == 'remain':
        for remain in data:
            if remain[3] <= val_ext:
                new_data.append(remain)

    answer = how_sort(new_data, sort_by)  

    return answer