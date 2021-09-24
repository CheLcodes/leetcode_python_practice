import collections
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        delta = [(1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1)]
        
        queue = collections.deque([[0, 0, 0]]) # start at (0, 0), 0 steps
        # vis = {(0, 0): True}
        vis = set()
        vis.add((0, 0))
        
        while queue:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return steps
            for dx, dy in delta:
                new_x, new_y = i + dx, j + dy
                if (new_x, new_y) not in vis:
                    vis.add((new_x, new_y))
                    queue.append([new_x, new_y, steps + 1])