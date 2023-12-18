import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # 对分数进行排序，使用dense方法从高到低进行排名，并添加一个新的rank列
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    # 删除id列
    scores.drop('id',axis=1,inplace = True)
    # 根据rank列进行升序排序
    scores.sort_values(by='rank',ascending=True,inplace=True)
    # 返回排序后的分数数据框
    return scores
