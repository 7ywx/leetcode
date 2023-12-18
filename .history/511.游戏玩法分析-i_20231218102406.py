import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
	activity['first_login'] = pd.to_datetime(activity['event_date'])
	activity['first_login'] = activity.groupby('player_id')['first_login'].transform('min')
	activity
