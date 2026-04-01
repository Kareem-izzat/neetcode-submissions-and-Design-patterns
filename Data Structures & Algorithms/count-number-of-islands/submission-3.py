from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    # Start BFS
                    queue = deque()
                    queue.append((i,j))
                    grid[i][j] = "0"  # mark visited

                    while queue:
                        r, c = queue.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"  # mark visited
                                queue.append((nr,nc))

                    # Finished exploring one island
                    count += 1

        return count