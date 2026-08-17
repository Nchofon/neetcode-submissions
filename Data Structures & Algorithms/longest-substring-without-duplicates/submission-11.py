class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxSub = 0  

        i =  0

        if len(s) <= 1:
            return len(s)

        count += 1
        for idx in range(1, len(s)):
            count += 1
            while s[idx] in s[i:idx]:
                i += 1
                count -= 1
            
            maxSub = max(maxSub, count)

        return maxSub


        