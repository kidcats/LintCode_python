def qsort(lists):
    if not lists:
        return []
    else:
        pro = lists[0]
        left = list(filter(lambda x : x < pro ,lists))
        right = list(filter(lambda x : x >= pro, lists[1:]))
        return qsort(left) + [pro] + qsort(right)

if __name__ == '__main__':
    a = [9,1,4,5,67,4,23,5,7]
    b = qsort(a)
    print(b)