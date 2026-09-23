class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(row, col):
            # inserts tuples into output
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0" or (row, col) in visited:
                return 

            visited.add((row, col))

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
            
        for row_index in range(ROWS):
            for col_index in range(COLS):
                if grid[row_index][col_index] == "1" and (row_index, col_index) not in visited:
                    islands += 1
                    dfs(row_index, col_index)

        return islands
    
    
