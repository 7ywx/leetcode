import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.drop_duplicates(subset='email',inplace=True)
    # print(person)
    # return person


data = {
    'id': [1, 2, 3],
    'email': ['john@example.com', 'bob@example.com', 'john@example.com']
}
person = pd.DataFrame(data)
delete_duplicate_emails(person)


# 创建示例数据
data1 = {'email': ['test1@example.com', 'test2@example.com', 'test1@example.com', 'test3@example.com'],
        'id': [10, 15, 5, 20]}
test = pd.DataFrame(data1)

# 删除重复的电子邮件，只保留一个具有最小 id 的唯一电子邮件
test.drop_duplicates(subset='email', keep='first', inplace=True)
print(test)
