#
# @lc app=leetcode.cn id=513 lang=python3
# @lcpr version=30104
#
# [513] 找树左下角的值
#
# https://leetcode.cn/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (73.66%)
# Likes:    626
# Dislikes: 0
# Total Accepted:    298.8K
# Total Submissions: 405.6K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
#
# 假设二叉树中至少有一个节点。
#
#
#
# 示例 1:
#
#
#
# 输入: root = [2,1,3]
# 输出: 1
#
#
# 示例 2:
#
# ⁠
#
# 输入: [1,2,3,4,null,5,6,null,null,7]
# 输出: 7
#
#
#
#
# 提示:
#
#
# 二叉树的节点个数的范围是 [1,10^4]
# -2^31 <= Node.val <= 2^31 - 1 
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1 # float('-inf')
        self.result = None
        self.dfs(root, 0)
        return self.result

        stack = [root]
        level_order = []
        while stack:
            tmp = []
            for _ in range(len(stack)): # 层序遍历
                cur = stack.pop(0)
                tmp.append(cur.val)
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)
            level_order.append(tmp)

        return level_order[-1][0]



    def dfs(self, node, depth):
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.result = node.val
            return

        if node.left:
            self.dfs(node.left, depth+1)
        if node.right:
            self.dfs(node.right, depth+1)
# @lc code=end



#
# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,null,5,6,null,null,7]\n
# @lcpr case=end

#
