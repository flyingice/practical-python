# mortgage.py
#
# Modified based on Exercise 1.8

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 1

extra_payment_start_month = int(input("Enter extra payment start month: "))
extra_payment_end_month = int(input("Enter extra payment end month: "))
extra_payment = float(input("Enter extra payment amount: "))

while principal > 0:
    actual_payment = (
        payment + extra_payment
        if month >= extra_payment_start_month and month <= extra_payment_end_month
        else payment
    )
    principal = principal * (1 + rate / 12) - actual_payment
    total_paid = total_paid + actual_payment
    month = month + 1

print("Total paid", total_paid)
print("Month required", month - 1)
