import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
     return pd.merge(employee.dropna(subset={'managerId'}),employee[['id', 'name']],left_on='managerId',right_on='id').groupby('managerId')[['id_x','name_y']].agg({'id_x':'count','name_y':'first'}).reset_index().query('id_x>=5')[['name_y']].rename(columns={'name_y':'name'})

    