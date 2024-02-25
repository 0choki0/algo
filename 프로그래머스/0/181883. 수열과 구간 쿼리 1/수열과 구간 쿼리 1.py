def solution(arr, queries):
    my_dict = {}
    for i in range(len(arr)):
        my_dict[i] = 0
    for query in queries:
        for i in range(query[0],query[1]+1):
            my_dict[i] += 1
    answer = []
    temp = 0
    for i in arr:
        answer.append(i+my_dict[temp])
        temp += 1
    return answer
        