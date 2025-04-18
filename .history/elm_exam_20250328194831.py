def can_rearrange_to_eleme(s: str) -> bool:
    # 统计e、l、m的数量
    count_e = s.count('e')
    count_l = s.count('l')
    count_m = s.count('m')

    # 判断条件
    if count_e >= count_l + count_m and count_l == count_m:
        return True
    else:
        return False

# 示例
s1 = "eeelm"
s2 = "eeelme"
print(can_rearrange_to_eleme(s1))  # 输出: True
print(can_rearrange_to_eleme(s2))  # 输出: False
