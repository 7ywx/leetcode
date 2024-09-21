#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#
# https://leetcode.cn/problems/same-tree/description/
#
# algorithms
# Easy (62.12%)
# Likes:    1175
# Dislikes: 0
# Total Accepted:    613K
# Total Submissions: 986.5K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
#
#
# 示例 1：
#
#
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
#
#
# 示例 3：
#
#
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
#
#
#
#
# 提示：
#
#
# 两棵树上的节点数目都在范围 [0, 100] 内
# -10^4
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = [p]
        queue_q = [q]
        while queue_p and queue_q:
            node_p = queue_p.pop(0)
            node_q = queue_q.pop(0)
            if node_p and node_q and node_p.val == node_q.val:
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)
            elif node_p == None and node_q == None:
                continue
            else:
                return False
        return True
# @lc code=end
