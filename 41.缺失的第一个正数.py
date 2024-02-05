#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode.cn/problems/first-missing-positive/description/
#
# algorithms
# Hard (43.83%)
# Likes:    2052
# Dislikes: 0
# Total Accepted:    350.5K
# Total Submissions: 798.6K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,0]
# 输出：3
#
#
# 示例 2：
#
#
# 输入：nums = [3,4,-1,1]
# 输出：2
#
#
# 示例 3：
#
#
# 输入：nums = [7,8,9,11,12]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1
# -2^31
#
#
#
import math
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # #TODO 搞清楚这个是什么方法
        # return min(set(range(1, len(nums) + 2)) - set(nums))

        # # 方法1：置换
        # # a.自己写的
        # nums_len = len(nums)
        # t, i = 0, 0
        # while i < nums_len:
        #     if nums[i] > 0 and nums[i] < nums_len and nums[nums[i] - 1] != nums[i]:
        #         t = nums[nums[i] - 1]
        #         nums[nums[i] - 1]= nums[i]
        #         nums[i] = t
        #         continue
        #     i += 1
        # for i, num in enumerate(nums):
        #     if num != i + 1:
        #         return i + 1
        # return nums_len + 1

        # b.chatgpt写的
        n = len(nums)

        # 将每个元素放置到正确的位置
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] #“多重赋值”或“序列解包赋值”。当你执行这样的赋值操作时，实际上是在同时计算右边表达式的值并将其按照从左到右的顺序赋给左边的变量

        # 再次遍历数组，找到第一个不在正确位置上的元素
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # 如果数组中所有元素都在正确位置上，则缺失的最小正整数是 n + 1
        return n + 1

        # # 方法2：哈希表
        # nums_dict = {num: True for num in nums}
        # i = 1
        # while True:
        #     if not nums_dict.get(i):
        #         return i
        #     i += 1
# @lc code=end
solution = Solution()
print(solution.firstMissingPositive([3,4,-1,1]))
