#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (38.57%)
# Likes:    1144
# Dislikes: 0
# Total Accepted:    220.6K
# Total Submissions: 572K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一个字符串数组 words。 words 中所有字符串 长度相同。
#
# s 中的 串联子串 是指一个包含  words 中所有字符串以任意顺序排列连接起来的子串。
#
#
# 例如，如果 words = ["ab","cd","ef"]， 那么 "abcdef"， "abefcd"，"cdabef"，
# "cdefab"，"efabcd"， 和 "efcdab" 都是串联子串。 "acdbef" 不是串联子串，因为他不是任何 words 排列的连接。
#
#
# 返回所有串联子串在 s 中的开始索引。你可以以 任意顺序 返回答案。
#
#
#
# 示例 1：
#
#
# 输入：s = "barfoothefoobarman", words = ["foo","bar"]
# 输出：[0,9]
# 解释：因为 words.length == 2 同时 words[i].length == 3，连接的子字符串的长度必须为 6。
# 子串 "barfoo" 开始位置是 0。它是 words 中以 ["bar","foo"] 顺序排列的连接。
# 子串 "foobar" 开始位置是 9。它是 words 中以 ["foo","bar"] 顺序排列的连接。
# 输出顺序无关紧要。返回 [9,0] 也是可以的。
#
#
# 示例 2：
#
#
# 输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# 输出：[]
# 解释：因为 words.length == 4 并且 words[i].length == 4，所以串联子串的长度必须为 16。
# s 中没有子串长度为 16 并且等于 words 的任何顺序排列的连接。
# 所以我们返回一个空数组。
#
#
# 示例 3：
#
#
# 输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# 输出：[6,9,12]
# 解释：因为 words.length == 3 并且 words[i].length == 3，所以串联子串的长度必须为 9。
# 子串 "foobarthe" 开始位置是 6。它是 words 中以 ["foo","bar","the"] 顺序排列的连接。
# 子串 "barthefoo" 开始位置是 9。它是 words 中以 ["bar","the","foo"] 顺序排列的连接。
# 子串 "thefoobar" 开始位置是 12。它是 words 中以 ["the","foo","bar"] 顺序排列的连接。
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] 和 s 由小写英文字母组成
#
#
#
from typing import List
from collections import Counter
import copy
# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        寻找字符串s中包含所有指定单词的子串的起始位置。

        :param s: 输入的字符串
        :param words: 一个单词列表，需要在s中找到这些单词
        :return: 一个列表，包含所有满足条件的子串的起始索引
        """

        # if not s or not words:return []
        # one_word = len(words[0])
        # word_num = len(words)
        # n = len(s)
        # if n < one_word:return []
        # words = Counter(words)
        # res = []
        # for i in range(0, one_word):
        #     cur_cnt = 0
        #     left = i
        #     right = i
        #     cur_Counter = Counter()
        #     while right + one_word <= n:
        #         w = s[right:right + one_word]
        #         right += one_word
        #         if w not in words:
        #             left = right
        #             cur_Counter.clear()
        #             cur_cnt = 0
        #         else:
        #             cur_Counter[w] += 1
        #             cur_cnt += 1
        #             while cur_Counter[w] > words[w]:
        #                 left_w = s[left:left+one_word]
        #                 left += one_word
        #                 cur_Counter[left_w] -= 1
        #                 cur_cnt -= 1
        #             if cur_cnt == word_num :
        #                 res.append(left)
        # return res


        if not s or not words:return []
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        words = Counter(words)
        res = []
        for i in range(0, one_word):
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                cur_Counter[w] += 1
                cur_cnt += 1
                while cur_Counter[w] > words[w]:
                    left_w = s[left:left+one_word]
                    left += one_word
                    cur_Counter[left_w] -= 1
                    cur_cnt -= 1
                if cur_cnt == word_num :
                    res.append(left)
        return res

        # if not s or not words:return []
        # one_word = len(words[0])
        # all_len = len(words) * one_word
        # n = len(s)
        # words = Counter(words)
        # res = []
        # for i in range(0, n - all_len + 1):
        #     tmp = s[i:i+all_len]
        #     c_tmp = []
        #     for j in range(0, all_len, one_word):
        #         c_tmp.append(tmp[j:j+one_word])
        #     if Counter(c_tmp) == words:
        #         res.append(i)
        # return res

        # 官方题解
        # # 初始化结果列表
        # res = []
        # # m: 单词列表中的单词数量, n: 每个单词的长度, ls: 输入字符串的长度
        # m, n, ls = len(words), len(words[0]), len(s)

        # # 遍历字符串s，以每个可能的单词为起点
        # for i in range(n):
        #     # 确保剩下的字符串长度足够包含所有单词
        #     if i + m * n > ls:
        #         break
        #     # 初始化一个计数器，用于统计当前考虑的字符串片段中各单词的出现次数
        #     differ = Counter()

        #     # 从i开始，遍历单词列表，构建当前考虑的字符串片段
        #     for j in range(m):
        #         word = s[i + j * n: i + (j + 1) * n]
        #         differ[word] += 1

        #     # 遍历单词列表，调整differ以反映需要匹配的单词及其数量
        #     for word in words:
        #         differ[word] -= 1
        #         if differ[word] == 0:
        #             del differ[word]

        #     # 从i开始，滑动窗口遍历字符串s，每次移动n个字符
        #     for start in range(i, ls - m * n + 1, n):
        #         # 如果不是第一次遍历，则更新differ
        #         if start != i:
        #             # 移除滑出窗口的单词，并更新differ
        #             word = s[start - n: start]
        #             differ[word] -= 1
        #             if differ[word] == 0:
        #                 del differ[word]
        #             # 添加新进入窗口的单词，并更新differ
        #             word = s[start + (m - 1) * n: start + m * n]
        #             differ[word] += 1
        #             if differ[word] == 0:
        #                 del differ[word]

        #         # 如果differ为空，说明找到了一个满足条件的子串
        #         if len(differ) == 0:
        #             res.append(start)

        # return res
# @lc code=end
print(Solution().findSubstring("barfoothefoobarman", ["foo","bar"]))
