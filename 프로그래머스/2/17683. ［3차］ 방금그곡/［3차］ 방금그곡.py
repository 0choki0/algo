def solution(m, musicinfos):
    answer = list()
    for music_info in musicinfos:
        st, et, title, sheet = music_info.split(",")
        
        # 재생 시간 계산
        st_hour, st_minute = st.split(":")
        et_hour, et_minute = et.split(":")
        st = 60*int(st_hour) + int(st_minute)
        et = 60*int(et_hour) + int(et_minute)
        time = et - st 

        # 치환
        melody = m.replace("C#", "c").replace("D#", "d").replace("E#", "e").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")
        sheet = sheet.replace("C#", "c").replace("D#", "d").replace("E#", "e").replace("F#", "f").replace("G#", "g").replace("A#", "a").replace("B#", "b")

        # 악보 작성
        sheet_len = len(sheet)
        quotient, remainder = divmod(time, sheet_len)
        remain = sheet[:remainder]
        sheet = sheet*quotient + remain

        # 멜로디가 악보에 있는지 확인
        if melody in sheet:
            answer.append([time, title])
    
    # answer list에서 답을 출력
    if not answer:
        return "(None)"
    else:
        temp = [0, ""]
        for time, title  in answer:
            if time > temp[0]:
                temp = [time, title]
        return temp[-1]
