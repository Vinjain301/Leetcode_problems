import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(candidates[candidates.years_of_exp>=2],rounds.groupby('interview_id')['score'].sum().reset_index(),on='interview_id').query('score>15')[['candidate_id']]
    