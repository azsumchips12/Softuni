number = int(input())
capacity = 255
water_counter = 0
for i in range(number):
    liters = int(input())
    if capacity - liters < 0:
        print("Insufficient capacity!")
        continue
    capacity -= liters
    water_counter += liters
print(water_counter)
