list1 = [10, 29, 14, 53, 2, 14]

for k in range(len(list1)):
    minimum = list1[k]
    index = 0
    for i in range(k + 1, len(list1)):
        if list1[i] < minimum:
            minimum = list1[i]
            index = i
    if index == 0:
        continue
    else:
        list1[k], list1[index] = list1[index], list1[k]

print(list1)
