def searchInsert(A, target):
        if len(A) == 0:
            return 0
        start,end=0,len(A)-1
        while start+1<end:
            mid=int((start+end)/2)
            if A[mid]<target:
                start=mid
            else:
                end=mid
        if A[start]>=target:
            return start
        if A[end]>=target:
            return end
        return len(A)

if __name__ =="__main__":
    a=[1,10,1001,201,1001,10001,10007]
    b=searchInsert(a,10008)