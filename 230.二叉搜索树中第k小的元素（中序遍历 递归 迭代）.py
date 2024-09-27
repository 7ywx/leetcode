#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (76.80%)
# Likes:    823
# Dislikes: 0
# Total Accepted:    328.6K
# Total Submissions: 427.7K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 树中的节点数为 n 。
# 1
# 0
#
#
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
#
#
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 递归
        inorder = []
        def dfs(root):
            if root.left: dfs(root.left)
            if root: inorder.append(root.val)
            if root.right: dfs(root.right)
        dfs(root)
        return inorder[k-1]

        # 迭代
        res = []
        stack = []
        i = 0
        while stack or root:
            # 先访问最左节点
            while root:
                stack.append(root)
                root = root.left
            # 再访问根
            root = stack.pop()
            res.append(root.val)
            i += 1
            if i == k:
                return res[-1]
            # 最后访问右节点
            root = root.right
# @lc code=end
def build_tree(nodes):
    if not nodes:
        return None

    root = TreeNode(nodes[0])
    queue = [root]
    i = 1

    while queue and i < len(nodes):
        current_node = queue.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)

        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)

        i += 1

    return root

# 用给定的节点列表构建二叉树
nodes_list = [3,1,4,None,2]
root = build_tree(nodes_list)

solution = Solution()
print(solution.kthSmallest(root, 1))
