class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """

    def subarraySum(self, nums):
        # write your code here
        start = 0
        while start + 1 < len(nums):
            a = nums[start + 1:]
            if nums[start] == 0 and nums[start + 1] != 0:
                return [start, start]
            sum = 0
            for i in range(len(a)):
                sum += a[i]
                if sum + nums[start] == 0:
                    return [start, start + i + 1]
            start += 1
        return [0, 0]