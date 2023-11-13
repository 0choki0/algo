def solution(wallpaper):
    c_wallpaper = [''.join(i) for i in zip(*wallpaper)]
    
    col = len(wallpaper[0])
    row = len(wallpaper)

    for i in range(row):
        if '#' in wallpaper[i]:
            top = i
            break
    for i in range(row-1, -1, -1):
        if '#' in wallpaper[i]:
            bottom = i + 1
            break
    for i in range(col):
        if '#' in c_wallpaper[i]:
            left = i
            break
    for i in range(col-1, -1, -1):
        if '#' in c_wallpaper[i]:
            right = i + 1
            break
    
    return [top, left, bottom, right]
