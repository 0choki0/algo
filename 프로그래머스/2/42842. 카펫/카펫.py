def solution(brown, yellow):
    side_block = brown - 4
    column = side_block // 4
    row = side_block // 4 + (side_block % 4) / 2
    while row * column != yellow:
        row += 1
        column -= 1
    return [row + 2, column + 2]