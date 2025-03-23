from typing import List
from typing import Optional
from 层序遍历构造二叉树 import buildTreeFromLevelOrder, levelOrder
#
# @lc app=leetcode.cn id=113 lang=python3
# @lcpr version=30005
#
# [113] 路径总和 II
#
# https://leetcode.cn/problems/path-sum-ii/description/
#
# algorithms
# Medium (63.21%)
# Likes:    1167
# Dislikes: 0
# Total Accepted:    449.5K
# Total Submissions: 706.1K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# 给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
#
# 叶子节点 是指没有子节点的节点。
#
#
#
#
#
# 示例 1：
#
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# 输出：[[5,4,11,2],[5,8,4,5]]
#
#
# 示例 2：
#
# 输入：root = [1,2,3], targetSum = 5
# 输出：[]
#
#
# 示例 3：
#
# 输入：root = [1,2], targetSum = 0
# 输出：[]
#
#
#
#
# 提示：
#
#
# 树中节点总数在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
#
#
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(root, visited, targetSum):
            """
            深度优先搜索（DFS）函数，用于寻找从根节点到叶子节点路径和等于给定值的路径。

            参数:
            root: 树的当前节点。
            visited: 已访问节点的值的列表，用于记录当前路径。
            targetSum: 目标和，即路径上所有节点值的总和需要匹配的值。

            返回: 无返回值。如果找到满足条件的路径，则将该路径添加到全局变量 ans 中。
            """
            # 定义 ans 为全局变量，用于存储所有满足条件的路径
            nonlocal ans

            # 如果当前节点为空，则直接返回，没有路径可探索
            if not root:
                return

            # 将当前节点的值添加到已访问路径中
            visited.append(root.val)

            # 检查当前节点是否为叶子节点
            if not root.left and not root.right:
                # 如果当前节点是叶子节点且节点值等于目标和，说明找到了一条满足条件的路径
                if targetSum == root.val:
                    # 将当前路径的副本添加到 ans 中
                    ans.append(visited[:])
                else:
                    # 如果当前节点值不等于目标和，移除当前节点值，回溯到上一层节点
                    visited.pop()
            # 对左子节点进行深度优先搜索，注意传递当前路径的副本和更新后的目标和
            dfs(root.left, visited[:], targetSum - root.val)
            # 对右子节点进行深度优先搜索，同样传递当前路径的副本和更新后的目标和
            dfs(root.right, visited[:], targetSum - root.val)

        dfs(root, [], targetSum)
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,4,8,11,null,13,4,7,2,null,null,5,1]\n22\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

s = Solution()
print(s.pathSum(buildTreeFromLevelOrder([5,4,8,11,None,13,4,7,2,None,None,5,1]), 22))
#
