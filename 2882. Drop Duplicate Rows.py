import pandas as pd

def dropDuplicateEmails(customers):
    # Drop duplicates, keeping the last occurrence
    # result = customers_df.drop_duplicates('email', keep='last')
    # False = remove all occurrences of duplicates
    return customers.drop_duplicates('email')

data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': [
        'emily@example.com',
        'michael@example.com',
        'sarah@example.com',
        'john@example.com',
        'john@example.com',
        'alice@example.com'
    ]
}

customers_df = pd.DataFrame(data)

unique_customers_df = dropDuplicateEmails(customers_df)

print(unique_customers_df)
