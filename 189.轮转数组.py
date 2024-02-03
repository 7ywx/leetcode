#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 轮转数组
#
# https://leetcode.cn/problems/rotate-array/description/
#
# algorithms
# Medium (44.50%)
# Likes:    2085
# Dislikes: 0
# Total Accepted:    786.4K
# Total Submissions: 1.8M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
#
#
#
# 示例 1:
#
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]
#
#
# 示例 2:
#
#
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]
# 解释:
# 向右轮转 1 步: [99,-1,-100,3]
# 向右轮转 2 步: [3,99,-1,-100]
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -2^31 <= nums[i] <= 2^31 - 1
# 0 <= k <= 10^5
#
#
#
#
# 进阶：
#
#
# 尽可能想出更多的解决方案，至少有 三种 不同的方法可以解决这个问题。
# 你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
#
#
#
import copy
from typing import Optional
from typing import List
# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 解法1：深拷贝
        nums_len = len(nums)
        temp = copy.deepcopy(nums)
        for i in range(nums_len):
            nums[(i+k)%nums_len] = temp[i]

        # 解法2：原地

        # 解法3：列表拼接实现轮转
        l = len(nums)
        k = k % l
        num1 = nums[0:l-k]
        num2 = nums[l-k::]
        num3 = num2 + num1
        for i in range(0, l):
            nums[i] = num3[i]

        # 解法4：数组切片拼接
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        #解法5：
        n = len(nums)  # 获取数组的长度
        newArr = [0] * n  # 创建一个与原数组大小相同的新数组
        for i in range(n):
            newArr[(i + k) % n] = nums[i]  # 将原数组中的元素按照旋转后的位置放入新数组中
        nums[:] = newArr  # 将新数组的内容复制回原数组（in-place修改）
# @lc code=end
Solution().rotate([1,2,3,4,5,6,7],3)
Solution().rotate([-1,-100,3,99], 2)
