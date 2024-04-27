#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (44.17%)
# Likes:    2896
# Dislikes: 0
# Total Accepted:    855.2K
# Total Submissions: 1.9M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
#
from typing import List, Optional
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        在旋转后的有序数组中查找目标值。

        参数:
        nums: 旋转后的有序数组，类型为list。
        target: 目标值，需要在数组中查找的元素。

        返回值:
        如果目标值存在于数组中，则返回其索引；否则返回-1。
        """





        # start = nums.index(min(nums))
        nums_len = len(nums) # 获取数组长度

        # 如果数组只有一个元素，直接判断是否为目标值，是则返回0，否则返回-1
        if nums_len == 1:
            return 0 if nums[0] == target else -1

        start = nums.index(min(nums)) # 找到数组中最小值的索引，即旋转点

        left, right = 0, nums_len - 1 # 初始化双指针

        while left <= right: # 二分查找
            # left + (right - left) // 2 可以防止left + right溢出
            mid = (left + right) // 2 # 计算中间位置
            mid_true = (mid + start) % nums_len # 考虑旋转后的真正中间位置

            if nums[mid_true] == target: # 如果找到目标值，返回其索引
                return mid_true
            elif target < nums[mid_true]: # 如果目标值小于中间位置的值，缩小右边界
                right = mid - 1
            else: # 如果目标值大于中间位置的值，增大左边界
                left = mid + 1
        return -1 # 如果未找到目标值，返回-1

        # v1 直接遍历数组，找到目标值并返回其索引
        for num in nums:
            if num == target:
                return nums.index(num)
        return -1
# @lc code=end
s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))
