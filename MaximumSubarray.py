def maxSubArray(nums):
    if len(nums) == 0 or nums is None:
        return nums
    maxsum = nums[0]
    minsum = 0
    sum = 0
    for num in nums:
        sum += num
        if sum - minsum > maxsum:
            maxsum = sum - minsum
        if sum < minsum:
            minsum = sum
    return maxsum

if __name__ =='__main__':
    ss = [-2,2,-3,4,-1,2,1,-5,3]
    print(maxSubArray(ss))