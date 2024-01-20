#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (52.87%)
# Likes:    1949
# Dislikes: 0
# Total Accepted:    521.4K
# Total Submissions: 988.5K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0
# -10^9
#
#
#
from typing import Optional
from typing import List
from collections import defaultdict
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 创建一个字典类型的变量result，用于存储列表nums中的元素及其出现次数
        result = defaultdict(list)
        # 将列表nums中的元素去除重复后，转换为排序后的列表，并存储为set_nums
        set_nums = sorted(list(set(nums)))
        # 初始化变量i为0
        i = 0
        # 初始化变量max_len为0，用于存储最长连续序列的长度
        max_len = 0
        # 循环遍历set_nums列表
        while i < len(set_nums):
            # 初始化变量sums为1
            sums = 1
            # 如果当前元素和下一个元素相差为1，则将sums加1，并将i加1
            while i < len(set_nums)-1 and set_nums[i]+1 == set_nums[i+1]:
                sums += 1
                i += 1
            # 如果sums大于max_len，则将max_len更新为sums
            if sums > max_len:
                max_len = sums
            # 将i加1
            i += 1
        # 返回最长连续序列的长度
        return max_len
# @lc code=end
solution = Solution()
solution.longestConsecutive([100,4,200,0,3,2])
