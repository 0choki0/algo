def solution(id_list, report, k):
    # id_list를 dictionary화
    id_dict = {}
    report_dict = {}
    for i in id_list:
        id_dict[i] = 0
        report_dict[i] = []
        
    # dict의 value를 [[신고한 사람들]] 로 저장
    for i in range(len(report)):
        report_detail = report[i].split(' ')
        report_dict[report_detail[1]].append(report_detail[0])

    # dict를 순회하면서 신고 횟수(중복x)가 k이상일 때, 신고자에게 메일 발송 
    for i in id_list:
        if len(set(report_dict[i])) >= k:
            for j in list(set(report_dict[i])):
                id_dict[j] += 1
    
    return list(id_dict.values())
