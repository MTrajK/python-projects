**FyleSDK** is the main class which is used to create a connection with Fyle APIs.

To make a connection with Fyle API you'll need to send Client ID, Client Secret, and Refresh Token as parameters in the FyleSDK constructor.

```python
from fylesdk import FyleSDK

connection = FyleSDK(
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>'
)
```

After this you're able to use all APIs like this (see more in the APIs section):

```python
"""
USAGE: <FyleSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Employees (with all available details for Employee)
response = connection.Employees.get()

# Get count of Reports updated on or after 2019-01-01
response = connection.Reports.count(updated_at='gte:2019-01-01T00:00:00.000Z')

# Create a new Expense of 10 USD, spent at 2019-01-01 and from an employee with email user@mail.com
new_expense = {
    'employee_email': 'user@mail.com',
    'currency': 'USD',
    'amount': 10,
    'spent_at': '2019-01-01T00:00:00.000Z',
    'reimbursable': True
}
response = connection.Expenses.post(new_expense)
```

The Fyle API access token expires after 3600 seconds (1 hour). If you need to refresh the access token, just call the **update_access_token** method from the created FyleSDK instance. 

```python
# Update the access token
response = connection.update_access_token()
```