import pandas as pd

def createBonusColumn(employees):
    # employees['bonus'] = employees['salary'] * 2
    # employees = employees.assign(bonus = employees['salary'] * 2)
    # employees['bonus'] = employees['salary'].apply(lambda x: x * 2)
    return employees


data = {
    'employee_id': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'salary': [50000, 60000, 55000, 70000, 80000]
}


employees_df = pd.DataFrame(data)


employees_df = createBonusColumn(employees_df)

print(employees_df)


# .assign(): df = df.assign(new_column=...)
# .apply(): df['new_column'] = df['existing_column'].apply(...)
# .loc[] for conditional assignment: df.loc[condition, 'new_column'] = ...
# numpy.where(): df['new_column'] = np.where(..., ..., ...)
# .insert(): df.insert(loc, 'new_column', ...)
# .concat(): df = pd.concat([df, new_column_df], axis=1)