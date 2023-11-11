def solution(my_string, is_suffix):
    if is_suffix not in my_string:
        return 0
    else:
        a = 0
        while True:
            if my_string[a:] == is_suffix:
                return 1
            else:
                a += 1
            if a == len(my_string):
                return 0