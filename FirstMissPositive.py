class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # write your code here
        if len(A) == 0:
            return 1
        b = [x for x in range(1, abs(max(A)) + 2)]
        for i in b:
            if A.count(i) == 0:
                return i