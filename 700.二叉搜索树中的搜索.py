#
# @lc app=leetcode.cn id=700 lang=python3
# @lcpr version=30104
#
# [700] 二叉搜索树中的搜索
#
# https://leetcode.cn/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (78.95%)
# Likes:    498
# Dislikes: 0
# Total Accepted:    375.5K
# Total Submissions: 475.4K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# 给定二叉搜索树（BST）的根节点 root 和一个整数值 val。
#
# 你需要在 BST 中找到节点值等于 val 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 null 。
#
#
#
# 示例 1:
#
#
#
# 输入：root = [4,2,7,1,3], val = 2
# 输出：[2,1,3]
#
#
# 示例 2:
#
# 输入：root = [4,2,7,1,3], val = 5
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点数在 [1, 5000] 范围内
# 1 <= Node.val <= 10^7
# root 是二叉搜索树
# 1 <= val <= 10^7
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # 如果根节点为空，则返回None，表示未找到指定值的节点
        if not root:
            return None

        # 如果指定值大于当前节点值，则在右子树中继续搜索
        if val > root.val:
            return self.searchBST(root.right, val)
        # 如果指定值小于当前节点值，则在左子树中继续搜索
        elif val < root.val:
            return self.searchBST(root.left, val)
        # 如果指定值等于当前节点值，则返回当前节点，表示找到了指定值的节点
        else:
            return root

# @lc code=end



#
# @lcpr case=start
# [4,2,7,1,3]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,2,7,1,3]\n5\n
# @lcpr case=end

#
