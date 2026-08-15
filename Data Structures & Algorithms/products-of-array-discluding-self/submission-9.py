
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rslt = [1] * n

        prefix = 1
        suffix = 1

        for i in range(n):
            rslt[i] *= prefix
            prefix *= nums[i]

            j = n - 1 - i
            rslt[j] *= suffix
            suffix *= nums[j]

        return rslt