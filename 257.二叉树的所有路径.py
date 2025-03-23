#
# @lc app=leetcode.cn id=257 lang=python3
# @lcpr version=30104
#
# [257] 二叉树的所有路径
#
# https://leetcode.cn/problems/binary-tree-paths/description/
#
# algorithms
# Easy (71.44%)
# Likes:    1217
# Dislikes: 0
# Total Accepted:    460.3K
# Total Submissions: 644.1K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#
# 示例 1：
#
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#
#
# 示例 2：
#
# 输入：root = [1]
# 输出：["1"]
#
#
#
#
# 提示：
#
#
# 树中节点的数目在范围 [1, 100] 内
# -100 <= Node.val <= 100
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def backtrack(node, path):
            if not node:
                return
            if not node.left and not node.right:
                res.append(path + str(node.val))
                return
            backtrack(node.left, path + str(node.val) + '->') # 回溯之道就在其中，“path + str(node.val)”这个表达式会生成一个新的str，但是path本身并没有改变
            backtrack(node.right, path + str(node.val) + '->')

        backtrack(root, '')
        return res

# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#
