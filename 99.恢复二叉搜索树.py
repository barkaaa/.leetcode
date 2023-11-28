#
# @lc app=leetcode.cn id=99 lang=python
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        
        treeList = []
        def dfs(root):
            if root:
                dfs(root.left)
                treeList.append(root)
                dfs(root.right)
        dfs(root)
        x = None
        y = None
        if len(treeList):
            pre = treeList[0]
            for i in range(1,len(treeList)):
                if pre.val > treeList[i].val:
                    
                    y = treeList[i]
                    if not x:
                        x = pre
                pre = treeList[i]
        if x and y :
            x.val,y.val = y.val,x.val

            
        
# @lc code=end

