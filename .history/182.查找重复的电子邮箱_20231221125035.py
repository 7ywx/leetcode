import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 找出重复的电子邮件
    duplicates = person_df[person_df.duplicated(subset='email')]['email']

    # 去除重复的电子邮件，确保每个电子邮件只出现一次
    unique_duplicates = duplicates.drop_duplicates()

    # 创建一个新的数据帧来保存重复的电子邮件
    duplicate_emails_df = pd.DataFrame({'Email': unique_duplicates})

    return duplicate_emails_df

# 创建示例数据
data = {'id': [1, 2, 3],
        'email': ['a@b.com', 'c@d.com', 'a@b.com']}
df = pd.DataFrame(data)

data1 = [
    {'id': 1, 'email': 'jacky@yahoo.com'},
    {'id': 2, 'email': 'jacky@yahoo.com'},
    {'id': 3, 'email': 'jacky@yahoo.com'}
]
df1 = pd.DataFrame(data1)
print(duplicate_emails(df1))
