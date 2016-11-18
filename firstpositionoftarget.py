def binarySearch(nums, target):
    if len(nums)==0:
        return -1
    start,end=0,len(nums)-1
    while start<end-1:
        mid=int((start+end)/2)
        if nums[mid]<target:
            start=mid
        else:
            end=mid
    if nums[start]==target:
        return start
    if nums[end]==target:
        return end
    return -1


if __name__=='__main__':
    a=binarySearch([5,9,9,15,15,18],15)
    print(a)
