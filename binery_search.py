def binery_search(list,target,start = 0, end = -1):
    start = start
    if end == -1:
        end = len(list) - 1
    else:
        end = end
    mid_index = int((start + end)/2)
    mid_num = list[mid_index]
    if target > mid_num:
        binery_search(list,target,start=mid_index+1)
    elif target < mid_num:
        binery_search(list,target,end=mid_index-1)
    elif target == mid_num:
        return mid_index


demo = [0,1,2,3,4,5,6,7,8,9]
print(binery_search(demo,9))
