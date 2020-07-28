from typing import List

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest: return 0
        res = 0
        trees = []
        for m in range(len(forest)):
            for n in range(len(forest[0])):
                if forest[m][n] >= 1:
                    trees.append((forest[m][n], m, n))
        trees.sort()
        x1, y1 = 0, 0
        for i in range(len(trees)):
            _, x2, y2 = trees[i]
            dis = self.bfs(x1, y1, x2, y2, forest)
            if dis == -1:
                return -1
            else:
                res += dis
                x1, y1 = x2, y2
        return res

    def bfs(self, x1, y1, x2, y2, forest):
        if (x1, y1) == (x2, y2): return 0
        queue, seen = [(x1, y1, 0)], set([x1, y1])
        while queue:
            r, c, dis = queue.pop(0)
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x, y = r + d[0], c + d[1]
                if (x, y) == (x2, y2):
                    return dis + 1
                if 0 <= x < len(forest) and 0 <= y < len(forest[0]) and forest[x][y] > 0 and (x, y) not in seen:
                    seen.add((x, y))
                    queue.append((x, y, dis + 1))
        return -1