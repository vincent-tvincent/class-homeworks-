def quick_sort(list, left=0, right=-1):
    if right == -1:
        R = len(list) - 1
    else:
        R = right
    L = left

    Range = range(L,R + 1)
    R_value = list[R]
    for p in Range:
        if list[p] < R_value:
            target = list[p]
            list.pop(p)
            list.insert(L, target)
            L += 1
    list[L],list[R] = list[R],list[L]

    if L < R:
        quick_sort(list,L,R - 1)
        quick_sort(list,left,L - 1)


L = [0,8,0,1,5,6,9,1,4,9]
quick_sort(L)
print(L)