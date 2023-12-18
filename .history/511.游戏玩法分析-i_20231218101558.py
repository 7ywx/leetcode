import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	a c['first_login'] = pd.to_datetime(df['event_date'])
	a c['first_login'] = a c.groupby('player_id')['first_login'].transform('min')
	a c.dropna(subset=['first_login'], inplace=True)
