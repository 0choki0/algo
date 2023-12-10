def solution(genres, plays):
    my_dict1 = {}
    my_dict2 = {}
    for n, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in my_dict1.keys():
            my_dict1[genre] = []
        my_dict1[genre].append((n, play))

        if genre not in my_dict2.keys():
            my_dict2[genre] = 0
        my_dict2[genre] += play

    answer = []
    for key, value in sorted(my_dict2.items(), key=lambda x:x[1], reverse=True):
        for n, play in sorted(my_dict1[key], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(n)

    return answer