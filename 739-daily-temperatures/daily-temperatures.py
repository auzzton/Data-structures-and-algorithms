class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #to store temp and its index
        for i, t in enumerate(temperatures):
            while len(stack)!=0 and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = (i - index)
            stack.append([t, i])
        return res
        