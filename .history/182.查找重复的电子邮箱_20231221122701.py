import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    # 找出所有重复的电子邮件
    duplicates = person[person.duplicated(subset='email',keep='first')]['email']
    print(duplicates)
    # 创建结果 DataFrame
    result = pd.DataFrame({'Email': duplicates})

    return result

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
