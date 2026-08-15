import string
import random
from collections import defaultdict

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        results = ""
        
        for word in strs:
            results += str(len(word)) + "#" + word

        print(results)
        return results

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            results.append(s[j+1 : j+1+length])
            i = j + 1 + length


        # while i < (len(s) - 2) :
            
        #     print(s[i+2 : i + 2 + int(s[i])])
        #     results.append( s[i+2 : i + 2 + int(s[i])] )
        #     print(i + 2 + int(s[i]))
        #     i =  i + 2 + int(s[i])


        return results
