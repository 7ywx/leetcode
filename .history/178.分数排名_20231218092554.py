import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    score_sorted = scores.sort_values(by=['score'], ascending=False)
