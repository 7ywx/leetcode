import pandas as pd
def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    # 合并两个 DataFrame，假设索引是相同的
    merged_df = person.merge(address, how='inner')
    return merged_df

# 假设的两个 DataFrame 示例
person = pd.DataFrame({'PersonId': [1, 2, 3], 'Name': ['John', 'Jane', 'Bob']})
address = pd.DataFrame({'PersonId': [1, 2, 4], 'Street': ['123 Main', '456 Elm', '789 Oak']})

# 创建一个示例DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

# 根据列名删除列
df = df.drop('col2', axis=1)

print(df)

# 调用函数
result = combine_two_tables(person, address)
print(result)
