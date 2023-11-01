# 1161. Maximum Level Sum of a Binary Tree

# Given the root of a binary tree, the level of its root is 1, 
# the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

# Example 1:
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.

# Example 2:
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# https://www.youtube.com/watch?v=7CgPNyJZ0xM

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[Treenode]) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        max_sum = float('-inf')
        min_level = 1

        while queue:
            level_size = len(queue)
            level_sum = 0

            for _ in range(level_size):
                curr_node, curr_level = queue.popleft()
                level_sum += curr_node.val

                if curr_node.left:
                    queue.append((curr_node.left, curr_level + 1))
                if curr_node.right:
                    queue.append((curr_node.right, curr_level + 1))

            if level_sum > max_sum:
                max_sum = level_sum
                min_level = curr_level

            return min_level