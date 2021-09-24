from collections import deque

class Solution:
    def findNearestLand(self, grid):
        m, n = len(grid), len(grid[0])
        val = [[float('inf')] * n for _ in grid]

        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            x, y, dis = queue.popleft()
            for d in delta:
                new_x, new_y = x + d[0], y + d[1]
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y]== float('inf') and val[new_x][new_y] > dis + 1:
                    val[new_x][new_y] = dis + 1
                    queue.append((new_x, new_y, dis + 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] in [-1, 0]:
                    val[i][j] = grid[i][j]
        
        return val


sol = Solution()
ans = sol.findNearestLand([[-1, 0, float('inf')], [float('inf'), 0, float('inf')], [float('inf'), -1, -1]])
print('ans:', ans)
