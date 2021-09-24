class Solution:

    def sameConnectedComponent(self, A, B):
        res = []
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] == B[i][j] == 1:
                    self.component = [(i, j)]
                    A[i][j] = B[i][j] = 0
                    if self.dfs(A, B, i, j, m, n):
                        res.append(self.component)
        return res
    

    def dfs(self, A, B, i, j, m, n):
        delta = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for d in delta:
            x, y = i + d[0], j + d[1]
            if 0 <= x < m and 0 <= y < n:
                if A[x][y] == B[x][y] == 1:
                    self.component.append((x, y))
                    A[x][y] = B[x][y] = 0
                    self.dfs(A, B, x, y, m, n)
                elif A[x][y] == B[x][y] == 0:
                    continue
                else:
                    return False
        return True


A = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
B = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

sol = Solution()
res = sol.sameConnectedComponent(A, B)
print(res)