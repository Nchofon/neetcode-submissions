from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kElements = Counter(nums)
        kSorted = sorted(kElements.items(), key=lambda items: items[1], reverse = True)
        # print(kSorted)
        
        return [key for key, val in kSorted[:k]]



        