month = input()
nights = int(input())

apartment_price = 0
studio_price = 0
if month == "May" or month == "October":
    apartment_price = 65 * nights
    studio_price = 50 * nights

elif month == "June" or month == "September":
    apartment_price = 68.7 * nights
    studio_price = 75.2 * nights

elif month == "July" or month == "August":
    apartment_price = 77 * nights
    studio_price = 76 * nights

if nights > 14 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.70
elif nights > 7 and (month == "May" or month == "October"):
    studio_price = studio_price * 0.95
elif nights > 14 and (month == "June" or month == "September"):
    studio_price = studio_price * 0.8

if nights > 14:
    apartment_price = apartment_price * 0.9

print(f"Apartment: {apartment_price:.2f} lv.")
print(f"Studio: {studio_price:.2f} lv.")