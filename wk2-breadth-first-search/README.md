# Week 2: Breadth First Search

## Problem 1
#problem description and/or link here#

## Problem 2
#problem description and/or link here#

## Problem 3
Find Bottom Left Tree Value (513)
https://leetcode.com/problems/find-bottom-left-tree-value/
#Solution:
from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return []
        cur_layer = deque([root])
        while len(cur_layer)>0:
            head_val = cur_layer[0].val
            next_layer = deque([])
            for ii in range(len(cur_layer)):
                cur_node = cur_layer.popleft()
                if cur_node.left != None:
                    next_layer.append(cur_node.left)
                if cur_node.right != None:
                    next_layer.append(cur_node.right)
                    
            cur_layer = next_layer
        return head_val

## Problem 4
Binary Tree Zigzag Level Order Traversal (103)
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
#Solution:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur_layer = deque([root])
        result = []
        LtoR = 1
        while len(cur_layer)>0:
            c_layer_val = []    
            next_layer = deque([])
            for ii in range(len(cur_layer)):
                cur_node = cur_layer.popleft()
                c_layer_val.append(cur_node.val)
                if cur_node.left != None:
                    next_layer.append(cur_node.left)
                if cur_node.right != None:
                    next_layer.append(cur_node.right)
                    
            if LtoR>0:
                result.append(c_layer_val)
            else:
                result.append(c_layer_val[::-1])
            LtoR *= -1
            cur_layer = next_layer
        return result

## Problem 5
#problem description and/or link here#

## Problem 6
#problem description and/or link here#

