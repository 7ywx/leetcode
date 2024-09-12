#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode.cn/problems/isomorphic-strings/description/
#
# algorithms
# Easy (49.56%)
# Likes:    735
# Dislikes: 0
# Total Accepted:    297.2K
# Total Submissions: 599.7K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t ，判断它们是否是同构的。
#
# 如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。
#
#
# 每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
#
#
#
# 示例 1:
#
#
# 输入：s = "egg", t = "add"
# 输出：true
#
#
# 示例 2：
#
#
# 输入：s = "foo", t = "bar"
# 输出：false
#
# 示例 3：
#
#
# 输入：s = "paper", t = "title"
# 输出：true
#
#
#
# 提示：
#
#
#
#
# 1 <= s.length <= 5 * 10^4
# t.length == s.length
# s 和 t 由任意有效的 ASCII 字符组成
#
#
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 使用字典存储s和t之间字符的映射关系
        fun = {}

        # 同时遍历s和t中的字符
        for x, y in zip(s, t):
            # 如果x不在fun中
            if x not in fun:
                # 如果y已经在fun的值中出现过，则返回False
                if y in fun.values():
                    return False
                # 将x映射到y
                fun[x] = y
            # 如果当前x映射的y与遍历到的y不同，则返回False
            if fun[x] != y:
                return False
        # 遍历结束，说明s和t同构
        return True

        # for i in range(l):
        #     if s[i] not in fun:
        #         if t[i] in fun.values():
        #             return False
        #         fun[s[i]] = t[i]
        #     if fun[s[i]] != t[i]:
        #         return False
        # return True
# @lc code=end
