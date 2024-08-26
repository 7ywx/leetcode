def build_index(t):
    index = {}
    last_pos = {}  # 存储每个字符第一次出现的位置
    for i, char in enumerate(t):
        if char not in last_pos:
            last_pos[char] = i
        index[char] = last_pos[char]
    return index

def is_subsequence(s, t, index):
    pos = -1  # 起始位置
    for char in s:
        if char not in index or index[char] <= pos:
            return False
        pos = index[char]
    return True

def process_strings(strings, t):
    index = build_index(t)
    for s in strings:
        yield is_subsequence(s, t, index)

# 假设 strings 是一个巨大的字符串列表
# 为了演示，这里使用一个小列表
strings = ["abc", "def", "ghi", "jkl"]

# 使用生成器处理字符串
results = process_strings(strings, "aabcdefghij")
# for result in results:
#     print(result)
print(results)
