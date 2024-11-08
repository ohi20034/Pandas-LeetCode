
import pandas as pd

def dropDuplicateEmails(customers):
    return customers.dropna(axis=0, how='any', subset=None, inplace=False)
    

data = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

df = pd.DataFrame(data)

result = dropDuplicateEmails(df)
print(result)


# df.dropna()	Drop rows with any missing values
# df.dropna(how='all')	Drop rows where all values are missing
# df.dropna(axis=1)	Drop columns with any missing values
# df.dropna(axis=0)	Drop row with any missing values
# df.dropna(subset=['column1', 'column2'])	Drop rows with missing values in specific columns
# df.dropna(inplace=True)	Drop missing data and modify the DataFrame in place