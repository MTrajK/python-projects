Here you can find all objects (schemas) with properties that are used in the Fyle API.

More details about the Fyle API Schemas you can find [here](https://app.swaggerhub.com/apis-docs/F588/Fyle_TPA/0.1).

### Employee

id, employee_email, employee_code, full_name, joining_date, location, level, business_unit, department, sub_department, approver1_email, approver2_email, approver3_email, title, branch_ifsc, branch_account, mobile, delegatee_email, default_cost_center_name, perdiem_names, mileage_rate_labels, custom_fields, disabled, org_id, org_name

### Expense

id, employee_id, employee_email, employee_code, spent_at, currency, amount, foreign_currency, foreign_amount, purpose, project_id, project_name, cost_center_id, cost_center_name, category_id, category_name, state, reimbursable, created_at, approved_at, verified, verified_at, reimbursed_at, vendor, has_attachments, attachments, custom_properties, org_id, org_name

### ExpenseCustomProperty

name, value

### Report

id, employee_id, employee_email, employee_code, state, amount, purpose, claim_number, transaction_ids, export_ids, created_at, approved_at, verified, verified_at, reimbursed_at, org_id, org_name

### Attachment

filename, content, password

### Category

id, name, code, enabled, fyle_category, sub_category, created_at, updated_at, org_id, org_name

### Advance

id, employee_id, employee_email, employee_code, org_id, org_name, project_id, project_name, currency, amount, purpose, issued_at, payment_mode, original_currency, original_amount, reference, exported, export_ids

### Refund

id, employee_id, employee_email, employee_code, collector_employee_id, collector_employee_email, collector_employee_code, returnee_employee_id, returnee_employee_email, returnee_employee_code, org_id, org_name, payment_mode, original_currency, original_amount, advance_account, reference, amount, note, exported, export_ids

### Reimbursement

id, employee_id, employee_email, employee_code, org_id, org_name, currency, amount, state, report_ids, unique_id, purpose, accounting_exported, exported, export_ids

### CustomUserField

custom_field_name, custom_field_value

### Location

city, state, country, display_name, formatted_address, latitude, longitude

### Project

id, name, description, active, approver1_employee_id, approver1_employee_email, approver1_employee_code, approver2_employee_id, approver2_employee_email, approver2_employee_code, org_id, org_name

### CostCenter

id, name, description, code, active, org_id, org_name

### BalanceTransfer

id, employee_id, employee_email, employee_code, issuer_employee_id, issuer_employee_email, issuer_employee_code, org_id, org_name, amount, currency, note, issued_at, created_at, source_account, exported, export_ids

### BulkError

row, key, message

### ExportNotify

object_id, object_type, status, description, reference, url, error, batch_id

### Export

id, object_id, object_type, exported_at, description, reference, url, error, status, batch_id, org_id, org_name, employee_id, employee_email, employee_code

### TripRequest

id, created_at, updated_at, traveller_details, requested_by, purpose, trip_notes, trip_type, trip_cities, project_id, project_name, updated_by, trip_state, request_number, custom_properties, is_sent_back, is_pulled_back, is_booked, is_requested_cancellation, start_date, end_date, org_id, org_name

### TransportationRequest

id, created_at, updated_at, requested_by, notes, from_city, to_city, trip_request_id, onward_at, return_at, request_number, assigned_to, assigned_at, transport_mode, preferred_timing, currency, amount, need_booking, custom_properties, org_id, org_name

### TransportationBooking

id, trip_request_id, booked_at, booked_by, transaction_id, booking_number, booking_reference_id, cancellation_requested, cancellation_requested_at, currency, booking_amount, notes, num_boarding_pass_files, org_id, org_name

### TransportationBookingCancellation

id, trip_request_id, cancelled_at, cancelled_by, transaction_id, cancellation_number, cancellation_reference_id, cancellation_currency, cancellation_amount, notes, num_boarding_pass_files, org_id, org_name

### HotelRequest

id, created_at, updated_at, requested_by, notes, city, location, trip_request_id, check_in_at, check_out_at, request_number, assigned_to, assigned_at, rooms, currency, amount, need_booking, custom_properties, org_id, org_name

### HotelBooking

id, trip_request_id, booked_at, booked_by, transaction_id, booking_number, booking_reference_id, cancellation_requested, cancellation_requested_at, currency, booking_amount, notes, num_boarding_pass_files, org_id, org_name

### HotelBookingCancellation

id, trip_request_id, cancelled_at, cancelled_by, transaction_id, cancellation_number, cancellation_reference_id, cancellation_currency, cancellation_amount, notes, org_id, org_name

### TravellerDetail

name, phone_number

### TripRequestCityDetails

from_city, to_city, onward_date, return_date
