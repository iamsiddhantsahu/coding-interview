# 2101. Detonate the Maximum Bombs

# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. 
# This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. 
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. 
# These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# https://www.youtube.com/watch?v=8NPbAvVXKR4

from typing import List
from collections import defaultdict
from math import sqrt

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list) # bomb -> [list of bombs]
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2)**2 + (y1 - y2)**2)

                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for nei in adj[i]:
                dfs(nei, visit)
            return len(visit)

        res = 0
        for i in range(len(bombs)):
            res = max(res, dfs(i, set()))
        return res

