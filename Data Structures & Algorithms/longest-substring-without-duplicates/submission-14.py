from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # count = 0
        # maxSub = 0  
        # i =  0

        # if len(s) <= 1:
        #     return len(s)

        # count += 1
        # for idx in range(1, len(s)):
        #     count += 1
        #     while s[idx] in s[i:idx]:
        #         i += 1
        #         count -= 1
            
        #     maxSub = max(maxSub, count)

        # return maxSub

        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len


        