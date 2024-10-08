#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode.cn/problems/design-add-and-search-words-data-structure/description/
#
# algorithms
# Medium (50.32%)
# Likes:    584
# Dislikes: 0
# Total Accepted:    96.4K
# Total Submissions: 191.2K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' + '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。
#
# 实现词典类 WordDictionary ：
#
#
# WordDictionary() 初始化词典对象
# void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
# bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。word 中可能包含一些
# '.' ，每个 . 都可以表示任何一个字母。
#
#
#
#
# 示例：
#
#
# 输入：
#
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# 输出：
# [null,null,null,null,false,true,true,true]
#
# 解释：
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // 返回 False
# wordDictionary.search("bad"); // 返回 True
# wordDictionary.search(".ad"); // 返回 True
# wordDictionary.search("b.."); // 返回 True
#
#
#
#
# 提示：
#
#
# 1 <= word.length <= 25
# addWord 中的 word 由小写英文字母组成
# search 中的 word 由 '.' 或小写英文字母组成
# 最多调用 10^4 次 addWord 和 search
#
#
#

# @lc code=start
class Node:
    def __init__(self):
        self.children = [None] * 26     # 子节点列表
        self.isEnd = False              # 标记是否尾节点
class WordDictionary:
    def __init__(self):
      self.root = Node()
    def addWord(self, word: str) -> None:
      cur = self.root
      for char in word:
        idx = ord(char) - ord('a')
        if cur.children[idx] is None:
          cur.children[idx] = Node()
        cur = cur.children[idx]
      cur.isEnd = True
    def search(self, word: str) -> bool:
        queue = [self.root]
        for i in range(len(word)):
            n = len(queue)
            if n == 0:
                return False
            for _ in range(n):
                node = queue.pop(0)
                if word[i] != '.':
                    index = ord(word[i]) - ord('a')
                    if node.children[index] is not None:
                        queue.append(node.children[index])
                else:
                    for child in node.children:
                        if child is not None:
                            queue.append(child)
        for node in queue:
            if node.isEnd:
                return True
        return False
      # def dfs(index: int, node: Node) -> bool:
      #       if index == len(word):
      #           return node.isEnd
      #       ch = word[index]
      #       if ch != '.':
      #           child = node.children[ord(ch) - ord('a')]
      #           if child is not None and dfs(index + 1, child):
      #               return True
      #       else:
      #           for child in node.children:
      #               if child is not None and dfs(index + 1, child):
      #                   return True
      #       return False

      # return dfs(0, self.root)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end
WD = WordDictionary()
WD.addWord("at")
WD.addWord("and")
WD.addWord("an")
WD.addWord("add")
print(WD.search("a"))
print(WD.search(".at"))
WD.addWord("bat")
print(WD.search(".at"))
print(WD.search("a.d."))
