import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # def opperate( opp: str, a: str, b: str) -> int:
        operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        myStack = []


        for t in tokens:
            if t in operations:
                b = myStack.pop()
                a = myStack.pop()
                myStack.append(int(operations[t](a, b)))
            else:
                myStack.append(float(t))

        return int(myStack[-1])



            


        