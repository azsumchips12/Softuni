project = input()
red = int(input())
colons = int(input())

total_place = red * colons
total_amount = 0

if project == 'Premiere':
    total_amount = total_place * 12
elif project == 'Normal':
    total_amount = total_place * 7.50
elif project == 'Discount':
    total_amount = total_place * 5
print(f"{total_amount:.2f} leva")