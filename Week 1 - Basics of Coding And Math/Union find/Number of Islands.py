class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self.dfs(grid, row, col)
        return count
    
    def dfs(self, grid, row, col):
        min_row = min_col = 0
        max_row = len(grid) - 1
        max_col = len(grid[0])- 1
        
        if (not min_row <= row <= max_row) or (not min_col <= col <= max_col):
            return 
        elif grid[row][col] != '1':
            return
        else:
            grid[row][col] = '0'
            self.dfs(grid, row+1, col)
            self.dfs(grid, row-1, col)
            self.dfs(grid, row, col+1)
            self.dfs(grid, row, col-1)
        