class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        lens = []

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == 0 or (row, col) in visited:
                return 

            visited.add((row, col))

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col)
                curr_island_size = len(visited)
                if curr_island_size not in lens:
                    lens.append(curr_island_size)
                    
        lens = lens[::-1]
        print(lens)
        for i in range(len(lens) - 1):
            lens[i] = lens[i] - lens[i + 1]
        print(lens)
        return max(lens)

