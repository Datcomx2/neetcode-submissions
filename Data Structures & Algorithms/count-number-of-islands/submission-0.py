class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            grid[r][c] = "0"
            dirs = [(1, 0), (0,1), (-1, 0), (0, -1)]
            for d in dirs:
                newR, newC = r + d[0], c + d[1]
                if ((0 <= newR < len(grid)) and (0 <= newC < len(grid[0]))
                 and grid[newR][newC] == "1"):
                 dfs(newR, newC)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r, c)
                    ans += 1
        
        return ans