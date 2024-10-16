from typing import List
#
# @lc app=leetcode.cn id=137 lang=python3
# @lcpr version=20001
#
# [137] 只出现一次的数字 II
#
# https://leetcode.cn/problems/single-number-ii/description/
#
# algorithms
# Medium (72.33%)
# Likes:    1254
# Dislikes: 0
# Total Accepted:    220.6K
# Total Submissions: 305K
# Testcase Example:  '[2,2,3,2]'
#
# 给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。
#
#
#
# 示例 1：
#
# 输入：nums = [2,2,3,2]
# 输出：3
#
#
# 示例 2：
#
# 输入：nums = [0,1,0,1,0,1,99]
# 输出：99
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -2^31 <= nums[i] <= 2^31 - 1
# nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
#
#
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1
        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        print(res)
        print(bin(res))
        print(bin(~0b11111111111111111111111111111100))
        print(bin(-4))
        print(bin(res ^ 0xffffffff))
        print(bin(~res))
        print(bin(~(res ^ 0xffffffff)))
        return res  # if counts[31] % m == 0 else -((res ^ 0xffffffff) + 1)
# @lc code=end



#
# @lcpr case=start
# [2,2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,1,0,1,0,1,99]\n
# @lcpr case=end

#
