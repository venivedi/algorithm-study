#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:38:56 2019

@author: dwang
"""

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