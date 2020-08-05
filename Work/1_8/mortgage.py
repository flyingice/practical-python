# mortgage.py
#
# Modified based on Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

while principal > 0:
    actual_payment = payment + 1000 if month < 12 else payment
    principal = principal * (1 + rate / 12) - actual_payment
    total_paid = total_paid + actual_payment
    month = month + 1

print("Total paid", total_paid)
print("Month required", month)
