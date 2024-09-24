#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#
# https://leetcode.cn/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (62.84%)
# Likes:    584
# Dislikes: 0
# Total Accepted:    276.8K
# Total Submissions: 440.3K
# Testcase Example:  '[4,2,6,1,3]'
#
# 给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
#
# 差值是一个正数，其数值等于两值之差的绝对值。
#
#
#
# 示例 1：
#
#
# 输入：root = [4,2,6,1,3]
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [1,0,48,null,null,12,49]
# 输出：1
#
#
#
#
# 提示：
#
#
# 树中节点的数目范围是 [2, 10^4]
# 0 <= Node.val <= 10^5
#
#
#
#
# 注意：本题与 783
# https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 中序遍历
        pre, ans = -1, float('inf')

        def dfs(node):
            nonlocal pre, ans
            if not node:
                return
            dfs(node.left)
            if pre != -1 and node.val - pre < ans:
                ans = node.val - pre
            pre = node.val
            dfs(node.right)

        dfs(root)
        return ans

        # 层序遍历得到节点值列表，排序，遍历求最小差值 （没有利用到二叉搜索树的性质）
        if not root: return 0
        queue = [root]
        nodeList = []
        while queue:
            node = queue.pop(0)
            nodeList.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        nodeList.sort()
        ans = float('inf')
        for i in range(1, len(nodeList)):
            ans = min(ans, nodeList[i] - nodeList[i-1])
        return ans
# @lc code=end
