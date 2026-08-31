class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        
        # Fill out the first row (can only come from the left)
        for c in range(1, n):
            grid[0][c] += grid[0][c - 1]
            
        # Fill out the first column (can only come from above)
        for r in range(1, m):
            grid[r][0] += grid[r - 1][0]
            
        # Fill out the rest of the grid
        for r in range(1, m):
            for c in range(1, n):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
                
        # The bottom-right corner holds the absolute minimum path sum
        return grid[-1][-1]