from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myAnagrams = defaultdict(list)
        for word in strs:
            # st = "".join(sorted(word))
            myAnagrams["".join(sorted(word))].append(word)
        return list(myAnagrams.values())
        