import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.sort_values('event_date').groupby('player_id')['event_date'].min().rename('first_login').reset_index()
    