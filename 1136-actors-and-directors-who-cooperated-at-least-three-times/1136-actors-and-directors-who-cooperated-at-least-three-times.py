import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    return actor_director.groupby(['actor_id','director_id'])['timestamp'].count().rename('cnt').reset_index().query('cnt>2')[['actor_id','director_id']]
   