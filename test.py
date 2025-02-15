
# stack = []

# # 检查变量是否为 None
# if stack is not None:
#     print("stack 不为 None")
# else:
#     print("stack 为 None")

# # 定义 ANSI 转义码
# RESET = "\033[0m"  # 重置颜色
# RED = "\033[0;31m"  # 红色

# # 原始字符串
# text = "Hello world"

# # 指定要突出显示的字符位置
# i = 4  # 例如，突出显示第6个字符（索引为5）

# # 构造突出显示的字符串
# highlighted_text = text[:i] + RED + text[i] + RESET + text[i+1:]

# # 打印突出显示的字符串
# print(highlighted_text)
# print("\033[0;31;44mHello world!\033[0m")  # 不高亮，红字，蓝底
# print("\033[1;31;40mHello world!\033[0m")  # 高亮，红字，黑底

test = set()
test.add(tuple([1]))
