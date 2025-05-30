import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return teacher.groupby('teacher_id')['subject_id'].nunique().rename('cnt').reset_index()
    