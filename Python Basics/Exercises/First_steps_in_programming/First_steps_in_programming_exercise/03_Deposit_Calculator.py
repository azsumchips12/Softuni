amount_deposited = float(input())
months = int(input())
year_procent = float(input())

per_year = amount_deposited * (year_procent / 100)
one_month = per_year / 12
final_price = amount_deposited + (months * one_month)

print(final_price)