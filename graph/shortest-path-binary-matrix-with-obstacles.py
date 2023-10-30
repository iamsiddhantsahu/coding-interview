# 1293. Shortest Path in a Grid with Obstacles Elimination

# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
# You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) 
# to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. 
# If it is not possible to find such walk return -1.

# Example 1:
# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

# Example 2:
# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.

# https://www.youtube.com/watch?v=VPleGcc1nZY

from typing import List
from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        target = (rows - 1, cols - 1)

        if k >= (rows - 1) + (cols - 1):
            return (rows - 1) + (cols - 1)

        queue = deque([(0, (0, 0, k))])
        seen = set([(0, 0, k)])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            steps, (row, col, obstacles) = queue.popleft()

            if (row, col) == target:
                return steps

            for row_inc, col_inc in directions:
                new_row = row + row_inc
                new_col = col + col_inc

                if (0 <= new_row < rows) and (0 <= new_col < cols):
                    new_obstacles = obstacles - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_obstacles)

                    if new_obstacles >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        return -1