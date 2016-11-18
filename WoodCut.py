def binarySearch(L, k):
    # write your code here
    if(len(L)==0):
            return 0
        L.sort()
        start=0
        end=L[len(L)-1]
        while start+1<end:
            mid=int((start+end)/2)
            sum=0
            for i in L:
                x=int(i/mid)
                sum+=x
            if sum==k:
                start=mid
            elif sum>k:
                start=mid
            else:
                end=mid
        return start


if __name__=='__main__':
    a=binarySearch([232, 124, 456],6)
    print(a)