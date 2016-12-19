def binarySearch(A,k):
    # write your code here
    index=0
    for i in range(k):
        index=deleteBig(A)
        A=A.replace(A[index],'',1)
        if A.startswith('0'):
            A=A[1:]
    return A

def deleteBig(A):
    for i in range(len(A)-1):
        if A[i+1]<A[i]:
            return i
    return len(A)-1

        


if __name__=='__main__':
    a=binarySearch('90249',1)
    print(a)