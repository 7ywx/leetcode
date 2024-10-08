#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (72.00%)
# Likes:    1612
# Dislikes: 0
# Total Accepted:    310.5K
# Total Submissions: 431.8K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' + '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Trie（发音类似 "try"）或者说 前缀树
# 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
#
# 请你实现 Trie 类：
#
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false
# 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true
# ；否则，返回 false 。
#
#
#
#
# 示例：
#
#
# 输入
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# 输出
# [null, null, true, false, true, null, true]
#
# 解释
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // 返回 True
# trie.search("app");     // 返回 False
# trie.startsWith("app"); // 返回 True
# trie.insert("app");
# trie.search("app");     // 返回 True
#
#
#
#
# 提示：
#
#
# 1
# word 和 prefix 仅由小写英文字母组成
# insert、search 和 startsWith 调用次数 总计 不超过 3 * 10^4 次
#
#
#

# @lc code=start
class Trie:
    def __init__(self):
      self.children = [None] * 26
      self.is_end_of_word = False

    def insert(self, word: str) -> None:
      for char in word:
        index = ord(char) - ord('a')
        if not self.children[index]:
          self.children[index] = Trie()
        self = self.children[index]
      self.is_end_of_word = True

    def search(self, word: str) -> bool:
      for char in word:
        index = ord(char) - ord('a')
        if not self.children[index]:
          return False
        self = self.children[index]
      if self.is_end_of_word != True:
        return False
      else:
        return True
    def startsWith(self, prefix: str) -> bool:
      for char in prefix:
        index = ord(char) - ord('a')
        if not self.children[index]:
          return False
        self = self.children[index]
      return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))

"""
字典树节点
"""
class Node:
    def __init__(self):
        self.children = [None] * 26     # 子节点列表
        self.isEnd = False              # 标记是否尾节点


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root      # 从根节点开始构造这个word对应的路径节点
        for char in word:
            # 将当前字符添加到当前节点对应的子节点位置，然后递归更新
            id_ = ord(char) - ord('a')
            if not node.children[id_]:
                node.children[id_] = Node()
            node = node.children[id_]
        node.isEnd = True # 最后一个节点的isEnd置为true，表示一个完整的字符串

    def search(self, word: str) -> bool:
        node = self.__search_prefix(word)
        return node != None and node.isEnd  # 返回不为空且节点标记为尾节点，则包含word这个完整的字符串

    def startsWith(self, prefix: str) -> bool:
        return self.__search_prefix(prefix) != None # 返回不为空，则包含了prefix前缀

    """
    查找字典树是否包含word前缀
    """
    def __search_prefix(self, word: str) -> Node:
        node = self.root  # 从根节点依次开始匹配每个字符
        for char in word:
            node = node.children[ord(char) - ord('a')]  # 根节点开始构造这个word对应的路径节点
            if not node:
                return     # 只要当前节点为空，则不包含这个字符串，直接返回空指针
        return node    # 否则匹配成功返回node
