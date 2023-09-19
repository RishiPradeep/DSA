mainlist = [29, 10, 14, 37, 14]


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return combine(left, right)


def combine(left, right):
    merged = []
    ri, li = 0, 0

    while ri < len(right) and li < len(left):
        if left[li] > right[ri]:
            merged.append(right[ri])
            ri += 1
        else:
            merged.append(left[li])
            li += 1

    merged.extend(right[ri:])
    merged.extend(left[li:])

    return merged


print(merge_sort(mainlist))
