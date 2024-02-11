# 1463. Cherry Pickup II

# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.

# Example 1:
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.

# Example 2:
# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.

from typing import List

class Solution:
    def cherryPickup_1(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}

        def dfs(r, c1, c2):
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            if c1 == c2 or min(c1, c2) < 0 or max(c1, c2) == COLS :
                return 0
            if r == ROWS - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0
            for c1_d in [-1, 0, 1]:
                for c2_d in [-1, 0, 1]:
                    res = max(
                        res,
                        dfs(r + 1, c1 + c1_d, c2 + c2_d)
                    )
            cache[(r, c1, c2)] = res + grid[r][c1] + grid[r][c2] 
            return cache[(r, c1, c2)]

        return dfs(0, 0, COLS-1)
    
    # more memory efficient
    def cherryPickup_2(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        dp = [[0] * COLS for _ in range(COLS)]

        for r in reversed(range(ROWS)):
            curr_dp = [[0] * COLS for _ in range(COLS)]
            for c1 in range(COLS - 1):
                for c2 in range(c1 + 1, COLS):
                    max_cherries = 0
                    cherries = grid[r][c1] + grid[r][c2]
                    for c1_d, c2_d in product([-1, 0, 1], [-1, 0, 1]):
                        nc1, nc2 = c1 + c1_d, c2 + c2_d
                        if nc1 < 0 or nc2 == COLS:
                            continue
                        max_cherries = max(
                            max_cherries,
                            cherries + dp[nc1][nc2]
                        )
                    curr_dp[c1][c2] = max_cherries
            dp = curr_dp
        return dp[0][COLS - 1]
        