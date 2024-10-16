#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#
# https://leetcode.cn/problems/single-number/description/
#
# algorithms
# Easy (73.13%)
# Likes:    3114
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 1.4M
# Testcase Example:  '[2,2,1]'
#
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#
#
#
#
#
# 示例 1 ：
#
#
# 输入：nums = [2,2,1]
# 输出：1
#
#
# 示例 2 ：
#
#
# 输入：nums = [4,1,2,1,2]
# 输出：4
#
#
# 示例 3 ：
#
#
# 输入：nums = [1]
# 输出：1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 3 * 10^4
# -3 * 10^4 <= nums[i] <= 3 * 10^4
# 除了某个元素只出现一次以外，其余每个元素均出现两次。
#
#
#
#
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 用逻辑运算符表示异或
        # （a & not b) or (not a & b)
        """
        异或运算的性质：
            - 任何数和自身异或都等于 0，即 a ⊕ a = 0。
            -任何数和 0 进行异或结果为该数本身，即 a ⊕ 0 = a。
        因此，如果数组中的元素出现了偶数次，那么它们的异或结果将会是 0。
        而只出现一次的元素只会和自身异或一次，其余的都会和另一个相同的元素异或两次，因此最终结果就是只出现一次的那个元素。

        举个例子来说明，假设数组为 [1, 2, 1, 3, 2]：

        对所有元素进行异或运算：1 ⊕ 2 ⊕ 1 ⊕ 3 ⊕ 2 = 3 ⊕ (1 ⊕ 1) ⊕ (2 ⊕ 2) = 3 ⊕ 0 ⊕ 0 = 3。
        只出现一次的元素是 3，其他元素都出现了两次，因此最终结果是 3。
        这就是为什么利用异或运算可以找出数组中只出现一次的元素的原因。
        """
        return reduce(lambda x, y: x ^ y, nums)
# @lc code=end
