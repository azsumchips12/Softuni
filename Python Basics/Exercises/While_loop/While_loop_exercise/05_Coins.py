money = float(input())
money_change = money * 100

count = 0

while money_change > 0:
    if money_change >= 200:
        money_change -= 200
    elif money_change >= 100:
        money_change -= 100
    elif money_change >= 50:
        money_change -= 50
    elif money_change >= 20:
        money_change -= 20
    elif money_change >= 10:
        money_change -= 10
    elif money_change >= 5:
        money_change -= 5
    elif money_change >= 2:
        money_change -= 2
    elif money_change >= 1:
        money_change -= 1

    else:
        break

    count = count + 1

print(count)
