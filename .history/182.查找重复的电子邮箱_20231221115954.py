import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:


# 创建示例数据
data = {'id': [1, 2, 3],
        'email': ['a@b.com', 'c@d.com', 'a@b.com']}
df = pd.DataFrame(data)
# 根据email列计算重复的电子邮件
duplicates = df[df.duplicated(subset='email')]

# 输出结果
print(duplicates)
