chicken_menu = int(input())
fish_menu = int(input())
vegatarian_menu = int(input())

chicken_price = chicken_menu * 10.35
fish_price = fish_menu * 12.40
vegatarian_price = vegatarian_menu * 8.15
all_menu_price = chicken_price + fish_price + vegatarian_price
dessert = 0.20 * all_menu_price
price_all = all_menu_price + 2.50 + dessert

print(price_all)