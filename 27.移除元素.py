#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
# https://leetcode.cn/problems/remove-element/description/
#
# algorithms
# Easy (59.52%)
# Likes:    2212
# Dislikes: 0
# Total Accepted:    1.5M
# Total Submissions: 2.5M
# Testcase Example:  '[3,2,2,3]\n3'
#
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
#
#
# 说明:
#
# 为什么返回数值是整数，但输出的答案是数组呢?
#
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
#
# 你可以想象内部操作如下:
#
#
# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而
# nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,3,0,4]
# 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0,
# 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
#
#
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        删除依据：

            remove(): 根据值来删除元素。它会移除列表中第一个匹配给定值的元素。如果该值不存在于列表中，则会抛出一个 ValueError 异常。
            pop(): 默认情况下根据索引来删除元素。它会移除并返回列表中指定索引位置的元素。如果不提供索引，默认移除并返回列表的最后一个元素。

        返回值：

            remove(): 不返回任何值（None），只修改列表。
            pop(): 返回被删除的元素的值。

        参数要求：

            remove(): 需要一个参数，即想要从列表中删除的元素的值。
            pop(): 可以接受一个参数（索引），如果不提供，则默认删除并返回最后一个元素。

        异常处理：

            使用 remove() 时，如果列表中没有该值，会抛出 ValueError。
            使用 pop() 时，如果索引超出了列表的范围，会抛出 IndexError。
        '''
        n = len(nums)
        popIndex = []
        for i in range(n):
            if nums[i] == val:
                popIndex.append(i)
                n -= 1
        for i in popIndex[::-1]:
            nums.pop(i)
        return n

        n = len(nums)
        valNum = nums.count(val)
        for i in range(valNum):
            nums.remove(val)
        return n - valNum
# @lc code=end
