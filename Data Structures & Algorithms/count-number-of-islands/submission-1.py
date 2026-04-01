class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        count=0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j]==False:
                    q = deque([(i,j)])
                    visited[i][j] = True

                    # Directions: up, down, left, right
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    while q:
                        r, c = q.popleft()
                        #print(r, c)  # process cell

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == "1":
                                visited[nr][nc] = True
                                q.append((nr, nc))
                    count+=1
        return count
        