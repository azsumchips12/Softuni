product = input()
city = input()
quantity = float(input())
price = 0

if city == 'Sofia':
    if product == 'coffee':
        price = 0.50
    elif product == 'water':
        price = 0.80
    elif product == 'beer':
        price = 1.2
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60

if city == 'Plovdiv':
    if product == 'coffee':
        price = 0.40
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50


if city == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.70
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55

whole_price = price * quantity
print(f'{whole_price}')
