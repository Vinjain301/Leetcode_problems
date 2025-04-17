import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    examinations['Number']=pd.Series(range(1,len(examinations)+1))
    exam=students.merge(subjects, how='cross')
    return pd.merge(exam,examinations.groupby(['student_id','subject_name']).count().rename(columns={'Number':'attended_exams'}).reset_index()[['student_id','subject_name','attended_exams']],on=['student_id','subject_name'],how='left').fillna({'attended_exams': 0}).sort_values(by=['student_id','subject_name']) 
    