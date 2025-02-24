budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())

video_cards_price = video_cards * 250
processors_price = processors * (video_cards_price * 0.35)
ram_price = ram * (video_cards_price * 0.1)

whole_price = video_cards_price + processors_price + ram_price

if video_cards > processors:
    whole_price = (whole_price - (whole_price * 0.15))

diff = abs(budget - whole_price)

if budget >= whole_price:
    print(f'You have {diff:.2f} leva left!')
else:
    print(f'Not enough money! You need {diff:.2f} leva more!')