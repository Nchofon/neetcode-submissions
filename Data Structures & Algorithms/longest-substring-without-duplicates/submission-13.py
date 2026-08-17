from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # myDict = defaultdict(list)
        # maxCount = 0

        # for i in range(len(s)):
        #     if s[i] in myDict:
        #         maxCount = max(i - myDict[s[i]][0], maxCount)
        #         myDict[s[i]].pop()
        #         myDict[s[i]].append(i)

        #     else :
        #         myDict[s[i]].append(i)
        #         maxCount = max(maxCount, 1)

        # return maxCount


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


        