from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # Count of islands
        count = 0

        # Directions to move: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        # Loop through every cell
        for i in range(rows):
            for j in range(cols):
                # If the cell is land ("1")
                if grid[i][j] == "1":
                    # Start BFS from this cell
                    q = deque()
                    q.append((i,j))
                    # Mark as visited by turning it into "0"
                    grid[i][j] = "0"

                    # Process the queue
                    while q:
                        r, c = q.popleft()
                        # Check all 4 neighbors
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            # If neighbor is inside grid and is land
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                q.append((nr,nc))
                                # Mark visited
                                grid[nr][nc] = "0"

                    # Finished exploring one island
                    count += 1

        return count