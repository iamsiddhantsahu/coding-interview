# 2050. Parallel Courses III

# You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
# You are also given a 2D integer array relations where relations[j] = [prevCoursej, nextCoursej] 
# denotes that course prevCoursej has to be completed before course nextCoursej (prerequisite relationship). 
# Furthermore, you are given a 0-indexed integer array time where time[i] denotes how many months it takes to 
# complete the (i+1)th course.

# You must find the minimum number of months needed to complete all the courses following these rules:

# You may start taking a course at any time if the prerequisites are met.
# Any number of courses can be taken at the same time.
# Return the minimum number of months needed to complete all the courses.

# Note: The test cases are generated such that it is possible to 
# complete every course (i.e., the graph is a directed acyclic graph).

# https://www.youtube.com/watch?v=a_NlRPnqCrg

from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        for src, dst in relations:
            adj[src].append(dst)
        
        max_time = {} #src -> max_time
        def dfs(src):
            if src in max_time:
                return max_time[src]
            
            res = time[src - 1]
            for nei in adj[src]:
                res = max(res, time[src - 1] + dfs(nei))
            max_time[src] = res
            return res
            
        for i in range(1, n+1):
            dfs(i)

        return max(max_time.values())

