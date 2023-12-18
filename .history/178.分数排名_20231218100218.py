import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    rank 函数的参数包括：

ascending: 排序方式，True为正序，False为降序。
method: 排序方法，包括'average', 'min', 'max', 'first', 'dense'。
na_option: 处理NaN的方式，包括'keep', 'top', 'bottom'。
pct: 是否返回百分比排名，True为返回百分比排名，False为返回绝对排名。
axis: 指定排序的轴，0为按行排序，1为按列排序。
其中，method 参数用来指定排序方法，常用的有以下几种：

'average': 使用平均排序，即在两个数值相同时，平均他们的排名。
'min': 使用最小排序，即在两个数值相同时，使用最小的排名。
'max': 使用最大排序，即在两个数值相同时，使用最大的排名。
'first': 使用固定排序，即在两个数值相同时，使用先前看到的第一个排名。
'dense': 使用紧凑排序，即在两个数值相同时，使用连续的排名（1, 2, 3, ...）。
na_option 参数用来指定处理 NaN 的方式，常用的有以下几种：

'keep': 保留原有的 NaN 排名。
'top': 将所有的 NaN 排名放在最前面。
'bottom': 将所有的 NaN 排名放在最后面。
pct 参数用来指定是否返回百分比排名，True 为返回百分比排名，False 为返回绝对排名。```
    # 对分数进行排序，使用dense方法从高到低进行排名，并添加一个新的rank列
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    # 删除id列
    scores.drop('id',axis=1,inplace = True)
    # 根据rank列进行升序排序
    scores.sort_values(by='rank',ascending=True,inplace=True)
    # 返回排序后的分数数据框
    return scores
