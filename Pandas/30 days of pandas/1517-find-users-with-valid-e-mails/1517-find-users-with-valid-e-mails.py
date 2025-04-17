import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[(users['mail'].str.split('@').str[1]=='leetcode.com') & (users['mail'].str.split('@').str[0].str.contains(r'^[a-zA-Z][a-zA-Z0-9_.-]*$', na=False)) ]  
    