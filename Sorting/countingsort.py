mainlist = [8, 5, 2, 6, 2, 4, 3, 2, 1, 2, 7, 7, 5, 6]
hashlist = {}
max = 0
for i in mainlist:
    if i >= max:
        max = i

for k in range(max + 1):
    hashlist[k] = 0

returnlist = []

for k in mainlist:
    if k in hashlist:
        hashlist[k] += 1

for k in hashlist:
    for i in range(hashlist[k]):
        returnlist.append(k)

print(returnlist)
