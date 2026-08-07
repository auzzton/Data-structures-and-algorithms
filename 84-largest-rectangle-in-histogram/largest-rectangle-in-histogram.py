class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = [] #stores index and height of current block
        marea = 0 # max area to return

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]: #height of the topmost stack
                index, height = stack.pop()
                marea = max(marea, height * (i - index))
                start = index
            stack.append((start, h))
        while stack:
            i, h = stack.pop()
            marea = max(marea, h * (len(heights) - i))
        return marea
        