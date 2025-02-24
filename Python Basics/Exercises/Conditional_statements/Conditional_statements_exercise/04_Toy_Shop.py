cost = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddy = int(input())
number_minion = int(input())
number_trucks = int(input())
price_everything = (number_puzzles * 2.60) + (number_dolls * 3) + (number_teddy * 4.10) + (number_minion * 8.20) + (number_trucks * 2)
everything_count = number_puzzles + number_dolls + number_teddy + number_minion + number_trucks

if everything_count >= 50:
    price_everything = price_everything - (price_everything * 0.25)

price_everything = price_everything - (price_everything * 0.1)
diff = abs(price_everything - cost)
if price_everything >= cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")