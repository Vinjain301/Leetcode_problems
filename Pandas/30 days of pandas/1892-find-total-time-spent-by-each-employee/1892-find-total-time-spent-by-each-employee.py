import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.groupby(['event_day','emp_id'])[['in_time','out_time']].apply(lambda x: (x['out_time']-x['in_time']).sum()).reset_index().rename(columns={'event_day':'day',0:'total_time'})
    
        