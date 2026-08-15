import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = str.maketrans('', '', string.punctuation + ' ')
        myS = s.translate(t)
        # print(myS)
        # print(s)

        return myS == "".join(myS[::-1])

        # s = s.replace(" ","").lower()
        # s = s.strip(string.punctuation)
        # return s == "".join(s[::-1])


        