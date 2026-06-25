class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ans = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    totalArea = self.dfs(r, c, grid)
                    ans = max(ans, totalArea )
        
        return ans
                

    def dfs(self, r: int, c: int, grid: List[List[int]]):
        grid[r][c] = 0
        area = 1
        dirs = [(1, 0), (0,1), (-1, 0), (0, -1)]
        for d in dirs:
            newR, newC = r + d[0], c + d[1]
            if (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])) and grid[newR][newC] == 1:
                area += self.dfs(newR, newC, grid)
        
        return area
