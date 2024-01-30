year_payment = int(input())

shoes = year_payment - (year_payment * 0.4)
suit = shoes - (shoes * 0.2)
ball = suit / 4
acces = ball / 5
whole_price = year_payment + shoes + suit + ball + acces
print(whole_price)