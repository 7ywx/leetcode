"""
1. 推箱子 WASD 能不能回到原点（0, 0）
2. 求区间内的幸运号码个数 幸运号码：存在能被3整除的连续子串 （010 = 10）
3. 最大队列整齐度 = 所有同学可以看见的同学总数 （同学只能向后看，且只能考到比自己矮的）
4. 最小字典序替换 给出两个字符串A，B和一个数组x，可以随意调增x，B中元素的位置。
   调整完后，遍历x，将A中第index_i元素替换为b中第i个元素（i为index_i在x中的索引）。
   要求：替换后的A‘与B的字典序最小
"""
def count_visible_students(heights):
    n = len(heights)
    total_visible = 0

    # 栈用来存储每个同学能看到的数量
    stack = []

    for i in range(n):
        visible_count = 0  # 当前同学能看到的同学数量

        # 从栈中弹出所有比当前同学矮的同学
        while stack and heights[stack[-1]] <= heights[i]:
            visible_count += 1
            stack.pop()

        # 当前同学能看到的同学是栈中剩下的所有
        visible_count += len(stack)

        # 加到总的可见人数
        total_visible += visible_count

        # 将当前同学入栈
        stack.append(i)

    return total_visible



def count_visible_students2(heights):
   ans = 0
   for i in range(len(heights)):
      for j in range(i+1, len(heights)):
         if heights[i] >= heights[j]:
            ans += 1
         else:
            ans += 1
            break
   return ans
#    ans = 0
#    postfix = [[0, 0]] * (len(heights)-1) + [[heights[-1], len(heights)-1]]
#    for i in range(len(heights)-2, -1, -1):
#       if heights[i] > postfix[i+1][0]:
#          postfix[i] = [heights[i], i]
#       else:
#          postfix[i] = postfix[i+1]
#    print(postfix)
#    for i, h in enumerate(heights):
#       if h == postfix[i][0]:
#          ans += len(heights) - i - 1
#          print(len(heights) - i - 1, end=" ")
#       else:
#          ans += postfix[i][1] - i
#          print(postfix[i][1] - i, end=" ")
#    print()
#    return ans
# 示例：
[10, 4, 3, 2, 7, 5]
heights = [43, 70, 72, 68, 43]
print(count_visible_students(heights))
# print(4+3+2+1)
# print(5+3+2+1+1)
import random

def generate_random_heights(n):
    """生成一个长度为n的随机高度数组"""
    return [random.randint(1, 10) for _ in range(n)]

def test_functions(num_tests=10000, max_length=5):
    """测试两个函数的返回值是否一致"""
    for _ in range(num_tests):
        # 生成随机数组长度
        n = random.randint(1, max_length)
        heights = generate_random_heights(n)

        # 调用两个函数
        result1 = count_visible_students(heights)
        result2 = count_visible_students2(heights)

        # 检查结果是否一致
        if result1 != result2:
            print(f"Test failed for heights: {heights}")
            print(f"count_visible_students returned: {result1}")
            print(f"count_visible_students2 returned: {result2}")
            return False

    print("All tests passed!")
    return True

# 运行测试
test_functions()
