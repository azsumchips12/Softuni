budget = float(input())
actors = int(input())
clothes_one = float(input())

decor = budget * 0.1
clothing = actors * clothes_one
if actors > 150:
    clothing = clothing * 0.90
all_price = decor + clothing
money_left = abs(budget - all_price)

if all_price > budget:
    print('Not enough money!')
    print(f'Wingard needs {money_left:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
