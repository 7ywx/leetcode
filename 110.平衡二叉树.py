#
# @lc app=leetcode.cn id=110 lang=python3
# @lcpr version=30104
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (59.17%)
# Likes:    1586
# Dislikes: 0
# Total Accepted:    696.5K
# Total Submissions: 1.2M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是 平衡二叉树  
#
#
#
# 示例 1：
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
# 示例 2：
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
# 示例 3：
#
# 输入：root = []
# 输出：true
#
#
#
#
# 提示：
#
#
# 树中的节点数在范围 [0, 5000] 内
# -10^4 <= Node.val <= 10^4
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root) != -1
    def dfs(self, root):
        """
        使用深度优先搜索（DFS）检查二叉树是否平衡。

        参数:
        root: TreeNode类型，表示二叉树的根节点。

        返回值:
        int类型，如果树是平衡的则返回树的高度，否则返回-1。
        """
        # 如果节点为空，返回高度0
        if not root: return 0

        # 递归计算左子树的高度
        left = self.dfs(root.left)
        # 递归计算右子树的高度
        right = self.dfs(root.right)

        # 如果左右子树高度差大于1，或任一子树不平衡，则返回-1
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1

        # 返回较大子树高度加1，表示当前节点的高度
        return max(left, right) + 1
# @lc code=end



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

#
