# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.

# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.

my_list = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
dic = {}

for i in my_list:
    if i in dic.keys(): # dic가 가지고 있는 key를 가져옴 
        dic[i] += 1 
    else:
        dic[i] = 1 # 첫번째 등장하는 key에 1의 value를 할당
print(dic)