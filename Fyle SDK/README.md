# FyleSDK

Python SDK for accessing Fyle APIs. [Fyle](https://www.fylehq.com/) is an expense management system.

## Installation

This project requires [Python 3+](https://www.python.org/downloads/) and [Requests](https://pypi.org/project/requests/) library (pip install requests).

1. Download this project and use it (copy it in your project, etc).
2. **Not available yet** - install it from [pip](https://pypi.org).

## Usage

To use this SDK you'll need these Fyle credentials used for OAuth2 authentication: **client ID**, **client secret** and **refresh token**.

This SDK is very easy to use.
1. First you'll need to create a connection using the main class FyleSDK.
```python
from fylesdk import FyleSDK

connection = FyleSDK(
    client_id='<YOUR CLIENT ID>',
    client_secret='<YOUR CLIENT SECRET>',
    refresh_token='<YOUR REFRESH TOKEN>'
)
```
2. After that you'll be able to access any of the 18 API classes: *Advances*, *BalanceTransfers*, *Categories*, *CostCenters*, *Employees*, *Expenses*, *Exports*, *HotelBookingCancellations*, *HotelBookings*, *HotelRequests*, *Projects*, *Refunds*, *Reimbursements*, *Reports*, *TransportationBookingCancellations*, *TransportationBookings*, *TransportationRequests*, *TripRequests*.
```python
"""
USAGE: <FyleSDK INSTANCE>.<API_NAME>.<API_METHOD>(<PARAMETERS>)
"""

# Get a list of all Employees (with all available details for Employee)
response = connection.Employees.get()

# Get count of Reports updated on or after 2019-01-01
response = connection.Reports.count(updated_at='gte:2019-01-01T00:00:00.000Z')

# Create a new Expense of 10 USD, spent at 2019-01-01 and from employee with email user@mail.com
new_expense = {
    'employee_email': 'user@mail.com',
    'currency': 'USD',
    'amount': 10,
    'spent_at': '2019-01-01T00:00:00.000Z',
    'reimbursable': True
}
response = connection.Expenses.post(new_expense)
```

See more details about the usage into the wiki pages of this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details