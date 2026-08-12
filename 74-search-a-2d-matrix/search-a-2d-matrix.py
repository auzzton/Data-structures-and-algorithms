class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        tot = m * n
        l = 0
        r  = tot - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            row = m // n
            col = m % n

            if matrix[row][col] == target:
                return True
            elif target > matrix[row][col]:
                l = m + 1
            else:
                r = m - 1
        return False
        