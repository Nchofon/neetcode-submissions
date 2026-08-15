class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        maxLen = 0
        curNum = 0
        curLen = 0

        for num in mySet:
            if num - 1 not in mySet:
                curNum = num
                curLen = 1
            
            while curNum + 1 in mySet:
                curNum += 1
                curLen += 1
            
            maxLen = max(maxLen, curLen)
        
        # for num in nums:
        #     if num in mySet:
        #         mySet.clear()
        #         maxCount = max(count, maxCount)
        #         count = 0

        #     else :
        #         mySet.add(num)
        #         count += 1

        return maxLen