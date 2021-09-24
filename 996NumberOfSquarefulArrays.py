from typing import List

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        A.sort()
        res = 0
        visited = [False] * len(A)
        res = self.dfs(A, visited, [], res)
        return res

    def dfs(self, A, visited, path, res):
        if len(path) == len(A):
            res += 1
            return res

        for i in range(len(A)):
            if not visited[i]:
                if i > 0 and not visited[i - 1] and A[i] == A[i - 1]:
                    continue
                if len(path) > 0 and not self.square(A[i], path[-1]):
                    continue

                path.append(A[i])
                visited[i] = True
                res = self.dfs(A, visited, path, res)
                visited[i] = False
                path.pop()
        return res

    def square(self, x, y):
        s = x + y
        return int(s ** 0.5) ** 2 == s

if __name__ == "__main__":
    res = Solution().numSquarefulPerms([1, 17, 8])
    print(res)


