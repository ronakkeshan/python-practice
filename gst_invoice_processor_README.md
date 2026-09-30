# GST Invoice Processor

A small billing system demonstrating OOP principles: a base `Invoice` class and a `DiscountedInvoice` subclass, with batch GST calculation across a mixed list of both types.

## What it does
- `Invoice`: stores invoice details (date, ID, customer, base amount, GST rate) and computes total, GST amount, and a readable description
- `DiscountedInvoice`: inherits from `Invoice`, applies a discount before calculating GST and total, and extends the description to show the discount rate
- `calculate_gst(invoices)`: sums GST across any list of invoices, regardless of type — works because each class defines its own `get_gst_amount()`, so the function never needs to check or branch on invoice type
- Handles bad/missing data defensively with `try/except`

## Design notes
- `calculate_gst` deliberately contains no logic specific to `Invoice` vs `DiscountedInvoice`. Each class reports its own correct GST amount, so adding a new invoice type later requires no changes to `calculate_gst` at all.
- `DiscountedInvoice.__str__` reuses `Invoice.__str__` via `super()` rather than duplicating the base description, then appends the discount info — so a future change to the base format only needs updating in one place.

## Why I built it
Practice applying inheritance and method overriding to a realistic business scenario — GST billing — rather than abstract examples. Reflects real invoicing concepts relevant to running Jai Shree Shyam Traders.

## Tech used
Python — classes, inheritance, `super()`, method overriding, exception handling