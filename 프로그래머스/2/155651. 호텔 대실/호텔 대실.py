def solution(book_time):
    room = 1
    room_list = dict()
    book_time.sort()

    # booking을 시간으로 변경 
    for check_in, check_out in book_time:

        # check_in을 int로 변경
        check_in_hour, check_in_minute = check_in.split(':')
        check_in = [int(check_in_hour), int(check_in_minute)]

        # check_out에 10분 추가
        check_out_hour, check_out_minute = check_out.split(':')
        if int(check_out_minute) < 50:
            check_out = [int(check_out_hour), int(check_out_minute)+10]
        else:
            check_out = [int(check_out_hour)+1, int(check_out_minute)-50]

        # room에 배정
        if len(room_list.keys()) == 0:
            room_list[room] = [check_in, check_out]

        else:
            for room_number, booking in room_list.items():
                if (check_out[0] < booking[0][0] or (check_out[0] == booking[0][0] and check_out[1] < booking[0][1])) or (check_in[0] > booking[1][0] or (check_in[0] == booking[1][0] and check_in[1] >= booking[1][1])):
                    room_list[room_number] = [check_in, check_out]
                    break
            else:
                room += 1
                room_list[room] = [check_in, check_out]

    return room