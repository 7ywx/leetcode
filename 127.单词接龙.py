#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# https://leetcode.cn/problems/word-ladder/description/
#
# algorithms
# Hard (49.09%)
# Likes:    1409
# Dislikes: 0
# Total Accepted:    229.4K
# Total Submissions: 467.1K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# 字典 wordList 中从单词 beginWord 到 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
#
#
# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
#
#
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
#
#
# 示例 1：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#
#
# 示例 2：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList =
# ["hot","dot","dog","lot","log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
#
#
#
# 提示：
#
#
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同
#
#
#

# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 将 wordList 转换为 HashSet，加速查找
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # 直接套用 BFS 算法框架
        q = collections.deque([beginWord])
        visited = set([beginWord])
        step = 1
        while q:
            sz = len(q)
            for i in range(sz):
                # 穷举 curWord 修改一个字符能得到的单词
                # 即对每个字符，穷举 26 个字母
                curWord = q.popleft()
                chars = list(curWord)
                # 开始穷举每一位字符 curWord[j]
                for j in range(len(curWord)):
                    originChar = chars[j]
                    # 对每一位穷举 26 个字母
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == originChar:
                            continue
                        chars[j] = c
                        # 如果构成的新单词在 wordSet 中，就是找到了一个可行的下一步
                        newWord = ''.join(chars)
                        if newWord in wordSet and newWord not in visited:
                            if newWord == endWord:
                                return step + 1
                            q.append(newWord)
                            visited.add(newWord)
                    # 最后别忘了把 curWord[j] 恢复
                    chars[j] = originChar
            # 这里增加步数
            step += 1
        return 0


# @lc code=end
