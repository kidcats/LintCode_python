class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """

    def productExcludeItself(self, A):
        # write your code her
        b = []
        for c in range(len(A)):
            tem = 1
            for i in A[:-1]:
                tem *= i
            b.append(tem)
            t = A.pop()
            A.insert(0, t)
        b.reverse()
        return b