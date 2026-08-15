class Solution:
    def isValid(self, s: str) -> bool:
        par = {'(':')', '{':'}', '[':']'}
        stack = []

        for i in range(len(s)):
            if s[i] in par:
                stack.append(s[i])
            else:
                if stack == [] or s[i] != par[stack[-1]]:
                    return False
                else :
                    stack.pop()
            
        return stack == []
