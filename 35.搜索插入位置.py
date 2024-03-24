#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode.cn/problems/search-insert-position/description/
#
# algorithms
# Easy (46.00%)
# Likes:    2279
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 3M
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 请必须使用时间复杂度为 O(log n) 的算法。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
#
# 示例 3:
#
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 为 无重复元素 的 升序 排列数组
# -10^4 <= target <= 10^4
#
#
#
from typing import List
# @lc code=sta
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        在给定的有序整数列表中，查找目标值出现的位置。如果目标值不存在，则返回它应该被插入的位置。

        参数:
        nums: List[int] -- 一个有序的整数列表。
        target: int -- 需要查找或插入的目标整数。

        返回值:
        int -- 目标值在列表中的索引，或者它应该被插入的位置。
        """
        nums_length = len(nums)
        left, right = 0, nums_length-1  # 初始化二分查找的左右边界

        # 处理目标值小于列表中最小值或大于列表中最大值的情况
        if target < nums[left]:
            return 0
        if nums[right] < target:
            return nums_length

        # 二分查找
        while left != right - 1:
            mid = (left + right) >> 1 # 二分查找的中点, (left + right) // 2
            if nums[mid] < target:  # 目标值在右半部分
                left = mid
            elif target < nums[mid]:  # 目标值在左半部分
                right = mid
            else:  # 找到目标值
                return mid

        # 检查最后的边界是否为目标值
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return right  # 如果目标值不存在，返回插入位置
# @lc code=end
s = Solution()
# print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3],1))
