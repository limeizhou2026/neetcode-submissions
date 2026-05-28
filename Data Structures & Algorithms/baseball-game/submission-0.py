class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = 0
        stack1 = []

        n = len(operations)
        for i in range(0, n):
            if operations[i] == "+":
               record = stack1[-1] + stack1[-2]
               stack1.append(record)
            elif operations[i] == "D":
                record = 2 * stack1[-1]
                stack1.append(record)
            elif operations[i] == "C":
                stack1.pop()
            else:
                record = int(operations[i])
                stack1.append(record)
        return sum(stack1)
            
        