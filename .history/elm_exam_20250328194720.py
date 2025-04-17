def is_eleme_string(s: str) -> bool:
    # 遍历字符串，检查是否存在不符合条件的子串
    for i in range(len(s) - 1):
        # 检查是否有连续的"ee", "lm", "ml", "ll", "mm"
        if (s[i] == 'e' and s[i+1] == 'e') or \
           (s[i] == 'l' and s[i+1] == 'm') or \
           (s[i] == 'm' and s[i+1] == 'l') or \
           (s[i] == 'l' and s[i+1] == 'l') or \
           (s[i] == 'm' and s[i+1] == 'm'):
            return False
    return True

# 测试
print(is_eleme_string("eeelm"))  # True
print(is_eleme_string("eeelme"))  # False
