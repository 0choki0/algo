my_list = [1, 5, 8, 2, 3, 1, 7, 9, 3, 5, 7]

counter = [i for i in range(10)]

for num in my_list:
    counter[num] += 1


result = []
for value, count in enumerate(counter):
    for i in range(count):
        result.append(value)