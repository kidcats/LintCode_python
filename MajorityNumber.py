def majorityNumber(self, nums):
        # write your code here
        if len(nums)==0:
            return -1
        nums.sort()
        return nums[len(nums)/2]

if __name__=='__mian__':
    a=majorityNumber([1,1,2,2,2])
    print(a)