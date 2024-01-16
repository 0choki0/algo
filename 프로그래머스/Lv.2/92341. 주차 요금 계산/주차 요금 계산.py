import math

def solution(fees, records):
    recording = {}
    enter = {}
    answer = []

    for record in records:
        record = record.split()
        if record[1] not in enter.keys():
            answer.append(record[1])
            enter[record[1]] = [record[0], record[2]]
            recording[record[1]] = 0
        else:
            if record[-1] == 'OUT':
                time = int(record[0][:2]) * 60 + int(record[0][3:]) - int(enter[record[1]][0][:2]) * 60 - int(enter[record[1]][0][3:])
                enter[record[1]] = [record[0], record[2]]
                recording[record[1]] += time
            else:
                enter[record[1]] = [record[0], record[2]]
    

    for key, value in enter.items():
        if value[-1] == 'IN':
            time = 24*60-1 - int(value[0][:2]) * 60 - int(value[0][3:])
            recording[key] += time

    result = []
    answer.sort()
    for i in answer:
        if recording[i] <= fees[0]:
            result.append(fees[1])
        else:
            result.append(fees[1] + math.ceil((recording[i] - fees[0])/fees[2])*fees[3])
    

    return result