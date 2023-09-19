mainlist = [29, 10, 14, 37, 14]


for k in range(1, len(mainlist)):
    smallest = True
    elem = mainlist.pop(k)
    for i in range(k - 1, -1, -1):
        if elem > mainlist[i]:
            mainlist.insert(i + 1, elem)
            smallest = False
            break
    if smallest:
        mainlist.insert(0, elem)
print(mainlist)
