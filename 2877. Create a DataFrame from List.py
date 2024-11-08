import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]):
    return pd.DataFrame(student_data,columns=['student_id','age'])

data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]


df = createDataframe(data)
print(df)