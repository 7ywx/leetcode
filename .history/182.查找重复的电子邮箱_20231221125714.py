import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 找出重复的电子邮件
    duplicates = person[person.duplicated(subset='email')]['email']

    # 去除重复的电子邮件，确保每个电子邮件只出现一次
    unique_duplicates = duplicates.drop_duplicates()

    # 创建一个新的数据帧来保存重复的电子邮件
    duplicate_emails_df = pd.DataFrame({'Email': unique_duplicates})

    return duplicate_emails_df

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 查找重复的邮箱
    df = person[person.duplicated('email')]
    # 只保留唯一的邮箱，转换为数据帧
    print(df.email.drop_duplicates().to_frame())
    return df.email.drop_duplicates().to_frame()
    # 对邮箱进行分组，并统计每个邮箱的数量，重命名列名为'cnt'
    person = person.groupby(by='email').size().reset_index(name='cnt')
    # 只保留出现次数大于1的邮箱，选择邮箱列，重命名列名为'Email'
    print(person[person['cnt'] > 1][['email']].rename(columns={'email':'Email'}))
    return person[person['cnt'] > 1][['email']].rename(columns={'email':'Email'})

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
print("---")
print(duplicate_emails(df1))
