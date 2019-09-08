Here you can find methods of all 18 API classes.

More details about the Fyle API parameters you can find [here](https://app.swaggerhub.com/apis-docs/F588/Fyle_TPA/0.1).

### Employees

Class for Employees APIs.

**Methods:**
* post(data) - Create or Update Employees in bulk.
* get(updated_at, offset, limit) - Get a list of existing Employees matching the parameters.
* count(update_at) - Get the count of existing Employees.

### Expenses

Class for Expenses APIs.

**Methods:**
* post(data) - Create an Expense for an Employee.
* get(updated_at, offset, limit, submitted) - Get a list of existing Expenses, excluding the file attachments, that match the parameters.
* count(update_at, exported, submitted) - Get the count of existing Expenses that match the given parameters.
* get_by_id(expense_id) - Get an Expense by Id including the file attachments.
* get_attachments(expense_id) - Get all the file attachments associated with an Expense.

### Reports

Class for Reports APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get a list of Reports.
* count(update_at, exported) - Get the count of Reports that match the parameters.

### Categories

Class for Categories APIs.

**Methods:**
* get(active_only) - Get a list of the existing Categories in the Organization.

### Advances

Class for Advances APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get a list of existing Advances.
* count(update_at, exported) - Get a count of the existing Advances that match the parameters.

### Refunds

Class for Refunds APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get a list of existing Refunds.
* count(update_at, exported) - Get the count of existing Refunds that match the parameters.

### Reimbursements

Class for Reimbursements APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get Reimbursments that satisfy the parameters.
* count(update_at, exported) - Get the number of Reimbursements that satisfy the parameters.

### Cost Centers

Class for CostCenters APIs.

**Methods:**
* get(active_only) - Get the list of existing CostCenters.

### Projects

Class for Projects APIs.

**Methods:**
* get(active_only) - Get the list of existing Projects.

### Balance Transfers

Class for BalanceTransfers APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get a list of existing Balance Transfers.
* count(update_at, exported) - Get the count of existing Balance Transfers.

### Exports

Class for ExportsAPIs.

**Methods:**
* post(data) - Mark Third Party Export of Fyle objects as Successful or Failed.
* get(updated_at, offset, limit) - Returns the details of Third Party Exports.
* count(update_at) - Returns the count of Third Party Exports, that satisfy the parameters.
* get_by_id(expense_id) - Get the details of a Third Party Export.

### Trip Requests

Class for TripRequests APIs.

**Methods:**
* get(updated_at, offset, limit, exported) - Get a list of existing Trip Request matching the parameters.
* count(update_at, exported) - Get the count of existing Trip Requests.

### Transportation Requests

Class for TransportationRequests APIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Transportation Request matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Transportation Requests.

### Transportation Bookings

Class for TransportationBookings APIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Transportation Booking matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Transportation Bookings.

### Transportation Booking Cancellations

Class for TransportationBookingCancellations APIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Transportation Booking Cancellations matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Transportation Booking Cancellations.

### Hotel Requests

Class for HotelRequests APIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Hotel Request matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Hotel Requests.

### Hotel Bookings

Class for HotelBookings APIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Hotel Booking matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Hotel Bookings.

### Hotel Booking Cancellations

Class for HotelBookingCancellationsAPIs.

**Methods:**
* get(trip_request_id, updated_at, offset, limit) - Get a list of existing Hotel Booking Cancellations matching the parameters.
* count(trip_request_id, update_at) - Get the count of existing Hotel Booking Cancellations.
