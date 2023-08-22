list1 = [10, 29, 14, 53, 2, 14]
swapped = True
while swapped:
    swapped = False
    for i in range(len(list1) - 1):
        if list1[i] > list1[i + 1]:
            list1[i], list1[i + 1] = list1[i + 1], list1[i]
            swapped = True
print(list1)

# O(N^2) time complexity
