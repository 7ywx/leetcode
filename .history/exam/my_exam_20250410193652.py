# def  f(n):
#     if n==0:
#         return 0
#     else:
#         return 1 + f(n&(n-1))
# print(f(15))

MOD = 10**9 + 7

# 快速幂算法
def mod_exp(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:  # exp是奇数
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def compute_result(s_n, n, k):
    # 计算2^k % MOD
    power_of_two = mod_exp(2, k, MOD)

    # 计算2^k - 1
    power_of_two_minus_one = (power_of_two - 1 + MOD) % MOD

    # 计算最终结果
    result = (s_n * power_of_two_minus_one + n) % MOD
    return result

# 示例：
s_n = 1
n = 5
k = 2

result = compute_result(s_n, n, k)
print(result)
