import pandas as pd

# def selectData(students):
#     result=students[students['student_id']==101]
#     return result[['name','age']]

# df.loc[<row_condition>, <column_selection>]
def selectData(students):
    return students.loc[students['student_id'] == 101, ['name', 'age']]


data = [
    [101, 'Ulysses', 13],
    [53, 'William', 10],
    [128, 'Henry', 6],
    [3, 'Henry', 11]
]
columns = ['student_id', 'name', 'age']

df = pd.DataFrame(data,columns=columns)

print(selectData(df))