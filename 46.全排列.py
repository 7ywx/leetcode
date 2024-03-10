#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode.cn/problems/permutations/description/
#
# algorithms
# Medium (79.02%)
# Likes:    2828
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3]'
#
# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [0,1]
# 输出：[[0,1],[1,0]]
#
#
# 示例 3：
#
#
# 输入：nums = [1]
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# nums 中的所有整数 互不相同
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #TODO 回溯 迭代 DNS
        """
        生成给定列表的所有全排列。

        参数:
        nums: List[int] - 需要生成全排列的整数列表。

        返回值:### 参数传递的方式
        """
        # v2.1 40ms左右 #TODO 没理解
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res

        # v2 30ms左右 used数组空间换时间 https://leetcode.cn/problems/permutations/solutions/9914/hui-su-suan-fa-python-dai-ma-java-dai-ma-by-liweiw
        def dfs(nums, size, depth, path, used, res):
            """
            深度优先搜索函数，用于生成所有可能的组合。

            :param nums: 给定的数字列表。
            :param size: 数字列表的大小。
            :param depth: 当前搜索的深度。
            :param path: 当前搜索路径。
            :param used: 标记哪些数字已被使用。
            :param res: 存储所有可能的组合结果。
            """
            # 当搜索深度等于列表大小时，将当前路径加入结果集
            if depth == size:
                '''
                path 参数传递是 值传递，对象类型变量在传参的过程中，复制的是变量的地址。
                这些地址被添加到 res 变量，但实际上指向的是同一块内存地址。
                在回溯中，一步步的path.pop()，由此我们会看到 6 个空的列表对象。
                所以需要path[:]，将当前路径的副本加入结果集(实拷贝)，而不是path本身。
                '''
                res.append(path[:])
                return

            # 遍历数字列表，尝试将未使用的数字加入当前路径
            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    # 递归进行下一层搜索
                    dfs(nums, size, depth + 1, path, used, res)

                    # 回溯：撤销上一步操作，标记该数字为未使用
                    used[i] = False
                    path.pop()

        size = len(nums)
        # 如果输入列表为空，直接返回空列表
        if len(nums) == 0:
            return []

        # 初始化用于标记数字使用情况的列表和存储结果的列表
        used = [False for _ in range(size)]
        res = []
        # 调用深度优先搜索函数
        dfs(nums, size, 0, [], used, res)
        # 返回所有可能的组合结果
        return res

        # v1 40ms左右
        # result = []  # 存储所有全排列结果的列表

        # # 如果列表元素个数小于2，则直接返回该列表作为唯一的一种排列
        # if len(nums) < 2:
        #     return [nums]

        # # 遍历列表中的每个元素
        # for num in nums:
        #     # 递归调用函数，生成不包含当前元素的所有排列
        #     temp = self.permute([item for item in nums if item != num])

        #     # 将当前元素依次添加到每种排列中，并将新的排列添加到结果列表中
        #     for t in temp:
        #         t.append(num)
        #         result.append(t)

        # return result
# @lc code=end
solution = Solution()
print(solution.permute([1,2,3]))
