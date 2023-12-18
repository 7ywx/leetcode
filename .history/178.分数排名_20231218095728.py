import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='first', ascending=False)
    scores.drop('id',axis=1,inplace = True)
	scores.
