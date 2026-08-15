class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     if nums[i] > target :
        #         continue 
        #     elif target - nums[i] in nums[i+1: len(nums)]:
        #         return [i, nums.index(target - nums[i])]
        
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1: len(nums)]:
                # s = nums[i+1: len(nums)]
                return [i, nums[i+1: len(nums)].index(target - nums[i])+i+1] 



        # return 
        